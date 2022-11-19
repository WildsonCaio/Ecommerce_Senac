from django.urls import path 
from . import views

urlpatterns = [ 
    path('', views.index, name='home'),
    path('details/<int:id>/', views.details, name='details'),
    path('cart/', views.cart, name='cart'),
    path('add_cart/<int:product>/', views.add_cart, name='add_cart'),
]