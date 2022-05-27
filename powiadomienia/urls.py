from django.urls import path
from .views import (
    PowiadomienieListView, 
    PowiadomienieDetailView, 
    PowiadomienieCreateView, 
    PowiadomienieUpdateView, 
    PowiadomienieDeleteView, 
    UserPowiadomienieListView,
    TestoweListView,
    PrzypomnieniaListView,
    WazneListView,
    KonkursyListView,
    InneListView
    )
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PowiadomienieListView.as_view(), name='powiadomienia-home'),
    path('testowe/', TestoweListView.as_view(), name='powiadomienia-testowe'),
    path('przypomnienia/', PrzypomnieniaListView.as_view(), name='powiadomienia-przypomnienia'),
    path('wazne/', WazneListView.as_view(), name='powiadomienia-wazne'),
    path('konkursy/', KonkursyListView.as_view(), name='powiadomienia-konkursy'),
    path('inne/', InneListView.as_view(), name='powiadomienia-inne'),
    path('user/<str:username>', UserPowiadomienieListView.as_view(), name='user-powiadomienia'),
    path('powiadomienie/<int:pk>/', PowiadomienieDetailView.as_view(), name='powiadomienie-detail'),
    path('powiadomienie/new/', PowiadomienieCreateView.as_view(), name='powiadomienie-create'),
    path('powiadomienie/<int:pk>/update/', PowiadomienieUpdateView.as_view(), name='powiadomienie-update'),
    path('powiadomienie/<int:pk>/delete/', PowiadomienieDeleteView.as_view(), name='powiadomienie-delete'), 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)