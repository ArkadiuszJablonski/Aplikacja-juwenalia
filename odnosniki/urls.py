from django.urls import path
from . import views
from .views import (
    OdnosnikListView,
    OdnosnikUpdateView,
    OdnosnikDeleteView,
)

urlpatterns = [
    path('', OdnosnikListView.as_view(), name='odnosniki-home'),
    path('odnosniki/new/', views.OdnosnikCreate, name='odnosniki-create'),
    path('odnosniki/<int:pk>/update/', OdnosnikUpdateView.as_view(), name='odnosniki-update'),
    path('odnosniki/<int:pk>/delete/', OdnosnikDeleteView.as_view(), name='odnosniki-delete'),
]