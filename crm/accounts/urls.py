from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customers/', views.customers),
    path('customer/<str:pk_test>/', views.customer),
    path('product/<str:pk_test>/', views.product),
]