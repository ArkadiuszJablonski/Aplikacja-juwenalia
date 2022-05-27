from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import OdnosnikForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Odnosnik

def home(request):
    context = {
        'links': Odnosnik.objects.all()
    }
    return render(request, 'odnosniki/home.html', context)

class OdnosnikListView(ListView):
    model = Odnosnik
    template_name = 'odnosniki/home.html' 
    context_object_name = 'odnosniki'

    def get_queryset(self):
        return Odnosnik.objects.all()

class OdnosnikUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Odnosnik
    fields = ['nazwa', 'link', 'zdjecie']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        odnosnik = self.get_object()
        if self.request.user.is_superuser:
            return True
        return False

class OdnosnikDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Odnosnik
    success_url = reverse_lazy('odnosniki-home')
    def test_func(self):
        odnosnik = self.get_object()
        if self.request.user.is_superuser:
            return True
        return False

def OdnosnikCreate(request):
    if request.method == 'POST':
        form = OdnosnikForm(request.POST, request.FILES)
        if form.is_valid():
            nazwa = form.cleaned_data['nazwa']
            link = form.cleaned_data['link']
            img = request.FILES.get('zdjecie')
            odnosnik_ = Odnosnik(nazwa=nazwa, link=link, zdjecie=img)
            odnosnik_.save()
            return redirect('odnosniki-home')
    else:
        form=OdnosnikForm()
    return render(request, 'odnosniki/odnosnik_form.html', {'form':form})