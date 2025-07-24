from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-to-cart/<int:car_id>/', views.add_to_cart, name='add_to_cart'),
]
