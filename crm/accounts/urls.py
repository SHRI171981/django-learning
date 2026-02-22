from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('products/', views.products, name='products'),
    path('customers/', views.customers, name='customers'),
    path('customer/<str:pk_test>/', views.customer, name='customer'),
    path('product/<str:pk_test>/', views.product, name='product'),

    path('create_order/<str:pk_test>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk_test>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk_test>/', views.deleteOrder, name='delete_order'),
]