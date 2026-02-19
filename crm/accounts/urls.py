from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customers/', views.customers, name='customers'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),
    path('product/<str:pk_test>/', views.product, name='product'),

    path('create_order/', views.createOrder, name='create_order'),
    path('update_order/<str:pk_test>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk_test>/', views.deleteOrder, name='delete_order'),
]