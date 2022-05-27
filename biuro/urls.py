from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='biuro-home'),
    path('lost/', views.add_lost_item, name='biuro-lost'),
    path('found/', views.add_found_item, name='biuro-found'),
    path('item/<int:id>', views.item_detail, name='item-detail'),
    path('delete/<int:id>', views.item_delete, name='item-delete'),
    path('waiting_list/', views.waiting_for_acceptation, name='biuro-waiting'),
    path('accepted/', views.items_accepted, name='biuro-accepted'),    
    path('waiting_list/<int:id>', views.acceptation_item_detail, name='acceptation-item-detail')

    # path('', views.home, name='biuro-home'),
]