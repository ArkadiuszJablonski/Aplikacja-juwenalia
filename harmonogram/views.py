from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Koncert


def home(request):
    return render(request, 'harmonogram/home.html')

class PlanListView(ListView):
    model = Koncert
    template_name = 'harmonogram/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'koncerty'
    paginate_by = 5;

    def get_queryset(self):
         return Koncert.objects.filter(uczestnicy__in=[self.request.user.id]).order_by('data_start')


class KoncertListView(ListView):
    model = Koncert
    template_name = 'harmonogram/koncerty.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'koncerty'
    ordering = ['data_start']
    paginate_by = 5;

    def get_queryset(self):
         return Koncert.objects.filter(rodzaj_wydarzenia='KO').order_by('data_start')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
            context['koncert_participation'] = Koncert.objects.filter(uczestnicy__in=[self.request.user]).distinct() 
        return context

class CzwartekListView(ListView):
    model = Koncert
    template_name = 'harmonogram/koncerty.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'koncerty'
    ordering = ['data_start']

    def get_queryset(self):
        return Koncert.objects.filter(data_start__range=["2019-05-09 00:00:00", "2019-05-09 23:59:00"]).order_by('data_start')


class PiatekListView(ListView):
    model = Koncert
    template_name = 'harmonogram/koncerty.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'koncerty'
    ordering = ['data_start']

    def get_queryset(self):
        return Koncert.objects.filter(data_start__range=["2019-05-10 00:00:00", "2019-05-10 23:59:00"]).order_by('data_start')


class SobotaListView(ListView):
    model = Koncert
    template_name = 'harmonogram/koncerty.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'koncerty'
    ordering = ['data_start']

    def get_queryset(self):
        return Koncert.objects.filter(data_start__range=["2019-05-11 00:00:00", "2019-05-11 23:59:00"]).order_by('data_start')

class KoncertDetailView(DetailView):
    model = Koncert
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        koncert = Koncert.objects.get(pk =self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user'] = self.request.user
        context['uczestnicy'] = koncert.uczestnicy.all()
        context['organizator'] = koncert.organizator
        #context['koncerty'] = Koncert.objects.filter(uczestnicy__in=[self.request.user]).distinct()     
        return context  

def koncerty_uczestnictwo_me(request, pk, operation):
    if operation == 'add':
        Koncert.take_part(request.user, pk)
    elif operation == 'remove':
        Koncert.remove_participation(request.user,pk)
    return redirect('koncerty-detail',pk=pk)

def koncerty_uczestnictwo_other(request, pk, operation, num):
    if operation == 'remove':
        user = get_object_or_404(User, pk=num)
        Koncert.remove_participation(user, pk)
    return redirect('koncerty-detail',pk=pk)
  
class KoncertCreateView(LoginRequiredMixin, CreateView):
    model = Koncert
    fields = ['rodzaj_wydarzenia', 'nazwa_wydarzenia', 'opis', 'data_start', 'data_koniec', 'miejsce_wydarzenia', 'zdjecie']

    def form_valid(self, form):
        form.instance.organizator = self.request.user
        return super().form_valid(form)


class KoncertUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Koncert
    fields = ['rodzaj_wydarzenia', 'nazwa_wydarzenia', 'opis', 'data_start', 'data_koniec', 'miejsce_wydarzenia', 'zdjecie']

    def form_valid(self, form):
        form.instance.organizator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        koncert = self.get_object()
        if self.request.user == koncert.organizator or self.request.user.is_superuser:
            return True
        return False
    

class KoncertDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Koncert
    success_url = reverse_lazy('harmonogram-koncerty')

    def test_func(self):
      koncert = self.get_object()
      if self.request.user == koncert.organizator or self.request.user.is_superuser:
          return True
      return False  
  
class TsportuListView(ListView):
    model = Koncert
    template_name = 'harmonogram/tydzien_sportu.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'koncerty'
    paginate_by = 5;

    def get_queryset(self):
         return Koncert.objects.filter(rodzaj_wydarzenia='TS').order_by('data_start')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
            context['koncert_participation'] = Koncert.objects.filter(rodzaj_wydarzenia='TS', uczestnicy__in=[self.request.user]).distinct() 
        return context    

class TsportuDetailView(DetailView):
    model = Koncert
    template_name = 'harmonogram/tydzien_sportu_detail.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        koncert = Koncert.objects.get(pk =self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user'] = self.request.user
        context['uczestnicy'] = koncert.uczestnicy.all()
        context['organizator'] = koncert.organizator
        #context['koncerty'] = Koncert.objects.filter(uczestnicy__in=[self.request.user]).distinct()     
        return context  

def tsportu_uczestnictwo_me(request, pk, operation):
    if operation == 'add':
        Koncert.take_part(request.user, pk)
    elif operation == 'remove':
        Koncert.remove_participation(request.user,pk)
    return redirect('tydzien-sportu-detail',pk=pk)

def tsportu_uczestnictwo_other(request, pk, operation, num):
    if operation == 'remove':
        user = get_object_or_404(User, pk=num)
        Koncert.remove_participation(user, pk)
    return redirect('tydzien-sportu-detail',pk=pk)

def tydz_sportu(request):
    return render(request, 'harmonogram/tydzien-sportu.html')

def tydz_kultury(request):
    return render(request, 'harmonogram/tydzien-kultury.html')

class TkulturyListView(ListView):
    model = Koncert
    template_name = 'harmonogram/tydzien_kultury.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'koncerty'
    paginate_by = 5;

    def get_queryset(self):
         return Koncert.objects.filter(rodzaj_wydarzenia='TK').order_by('data_start')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
            context['koncert_participation'] = Koncert.objects.filter(rodzaj_wydarzenia='TK', uczestnicy__in=[self.request.user]).distinct() 
        return context    

class TkulturyDetailView(DetailView):
    model = Koncert
    template_name = 'harmonogram/tydzien_kultury_detail.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        koncert = Koncert.objects.get(pk =self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user'] = self.request.user
        context['uczestnicy'] = koncert.uczestnicy.all()
        context['organizator'] = koncert.organizator
        #context['koncerty'] = Koncert.objects.filter(uczestnicy__in=[self.request.user]).distinct()     
        return context  

def tkultury_uczestnictwo_me(request, pk, operation):
    if operation == 'add':
        Koncert.take_part(request.user, pk)
    elif operation == 'remove':
        Koncert.remove_participation(request.user,pk)
    return redirect('tydzien-kultury-detail',pk=pk)

def tkultury_uczestnictwo_other(request, pk, operation, num):
    if operation == 'remove':
        user = get_object_or_404(User, pk=num)
        Koncert.remove_participation(user, pk)
    return redirect('tydzien-kultury-detail',pk=pk)    

