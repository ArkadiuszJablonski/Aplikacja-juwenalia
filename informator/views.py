from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post, Photo
from django.contrib import messages
from .forms import ImageUploadForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def home(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request, 'informator/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'informator/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'informator/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['tytul', 'tresc']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['tytul', 'tresc']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('informator-home')
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def galeria(request):
    queryset = Photo.objects.all()
    context = {
        'photos': queryset
        }
    return render(request, 'informator/galeria.html', context)


class PhotoListView(ListView):
    model = Photo
    template_name = 'informator/galeria.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'photos'
    ordering = ['-date_posted']
    paginate_by = 12


class PhotoDetailView(DetailView):
    model = Photo


class PhotoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    fields = ['opis', 'zdjecie']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        photo = self.get_object()
        if self.request.user == photo.author or self.request.user.is_superuser:
            return True
        return False

class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('informator-galeria')
    def test_func(self):
        photo = self.get_object()
        if self.request.user == photo.author or self.request.user.is_superuser:
            return True
        return False


def PhotoAdd(request):
    form_class = Photo.objects.all()
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = Photo(opis=request.POST.get("opis"), zdjecie=request.FILES['zdjecie'], author=request.user)
            m.save()
            messages.success(request, f'Dodano nowe zdjecie!')
            return redirect('informator-galeria')
    else:
        form = ImageUploadForm()

    return render(request, 'informator/photo_form.html', {'form':form})


def mapa(request):
    return render(request, 'informator/mapa.html')


