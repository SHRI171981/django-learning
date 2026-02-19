from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Customer, Order

# Dashboard view
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customers(request):
    customers = Customer.objects.all()
    return render(request, 'accounts/customer.html', {'customers': customers})


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count
    }
    return render(request, 'accounts/single_customer.html', context)


def product(request, pk_test):
    product = Product.objects.get(id=pk_test)
    context = {
        'product': product
    }
    return render(request, 'accounts/single_product.html', context)