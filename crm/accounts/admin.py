from django.contrib import admin
from .models import Customer, Product, Order

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date_created')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description', 'date_created')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'status')