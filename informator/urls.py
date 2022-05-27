from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    UserPostListView,
    PhotoListView,
    PhotoDetailView,
    PhotoUpdateView, 
    PhotoDeleteView
    )
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostListView.as_view(), name='informator-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 
    path('galeria/', PhotoListView.as_view(), name='informator-galeria'),
    path('galeria/new/', views.PhotoAdd, name='photo-create'),
    path('galeria/zdjecie/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail'),
    path('galeria/zdjecie/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo-update'),
    path('galeria/zdjecie/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo-delete'),
    path('mapa/', views.mapa, name='informator-mapa'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)