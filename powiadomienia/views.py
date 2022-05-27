from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Powiadomienie
from django.contrib import messages

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def home(request):
    context ={
        'powiadomienia': Powiadomienie.objects.all()
    }
    return render(request, 'powiadomienia/home.html', context)

class PowiadomienieListView(ListView):
    model = Powiadomienie
    template_name = 'powiadomienia/home.html' 
    context_object_name = 'powiadomienia'
    paginate_by = 5

    def get_queryset(self):
        return Powiadomienie.objects.exclude(kategoria='testowe').order_by('-date_posted')

# testowe widoczne tylko po recznej zmianie adresu w przegladarce
class TestoweListView(ListView):
    model = Powiadomienie
    template_name = 'powiadomienia/home.html' 
    context_object_name = 'powiadomienia'
    paginate_by = 5

    def get_queryset(self):
        return Powiadomienie.objects.filter(kategoria='testowe').order_by('-date_posted')

class PrzypomnieniaListView(ListView):
    model = Powiadomienie
    template_name = 'powiadomienia/home.html' 
    context_object_name = 'powiadomienia'
    paginate_by = 5

    def get_queryset(self):
        return Powiadomienie.objects.filter(kategoria='Przypomnienie o wydarzeniu').order_by('-date_posted')

class KonkursyListView(ListView):
    model = Powiadomienie
    template_name = 'powiadomienia/home.html'
    context_object_name = 'powiadomienia'
    paginate_by = 5

    def get_queryset(self):
        return Powiadomienie.objects.filter(kategoria='Konkursy').order_by('-date_posted')

class WazneListView(ListView):
    model = Powiadomienie
    template_name = 'powiadomienia/home.html' 
    context_object_name = 'powiadomienia'
    paginate_by = 5

    def get_queryset(self):
        return Powiadomienie.objects.filter(kategoria='Ważne informacje').order_by('-date_posted')

class InneListView(ListView):
    model = Powiadomienie
    template_name = 'powiadomienia/home.html' 
    context_object_name = 'powiadomienia'
    paginate_by = 5

    def get_queryset(self):
        return Powiadomienie.objects.filter(kategoria='Inne').order_by('-date_posted')


class UserPowiadomienieListView(ListView):
    model = Powiadomienie
    template_name = 'powiadomienia/user_powiadomienia.html' 
    context_object_name = 'powiadomienia'
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Powiadomienie.objects.filter(author=user).order_by('-date_posted')

class PowiadomienieDetailView(DetailView):
    model = Powiadomienie

class PowiadomienieCreateView(LoginRequiredMixin, CreateView):
    model = Powiadomienie
    fields = ['nazwa', 'treść', 'kategoria', 'odbiorcy']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PowiadomienieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Powiadomienie
    fields = ['nazwa', 'treść', 'kategoria', 'odbiorcy']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        powiadomienie = self.get_object()
        if self.request.user == powiadomienie.author:
            return True
        return False

class PowiadomienieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Powiadomienie
    success_url = '/powiadomienia/'
    def test_func(self):
        powiadomienie = self.get_object()
        if self.request.user == powiadomienie.author:
            return True
        return False

