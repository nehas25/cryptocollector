from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coins/', views.index, name='index'),
    path('coins/new/', views.add_coin, name='add_coin'),
    path('coins/<int:coin_id>/', views.coins_detail, name='coins_detail'),
    path('coins/<int:coin_id>/edit/', views.coins_edit, name='coins_edit'),
    path('coins/<int:coin_id>/delete/', views.coins_delete, name='coins_delete'),
    path('coins/<int:coin_id>/historical_data/', views.coins_add_historical_data, name='coins_add_historical_data'),
    path('coins/<int:coin_id>/exchange/<int:exchange_id>/add/', views.add_exchange, name='add_exchange'),
    path('coins/<int:coin_id>/exchange/<int:exchange_id>/remove/', views.remove_exchange, name='remove_exchange'),
]