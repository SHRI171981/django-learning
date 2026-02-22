from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import Product, Customer, Order
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is not matched')
    return render(request, 'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


# Dashboard view
@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs # qs is the filtered queryset

    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'myFilter': myFilter
    }

    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


@login_required(login_url='login')
def customers(request):
    customers = Customer.objects.all()
    return render(request, 'accounts/customer.html', {'customers': customers})


@login_required(login_url='login')
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count,
    }
    return render(request, 'accounts/single_customer.html', context)


@login_required(login_url='login')
def product(request, pk_test):
    product = Product.objects.get(id=pk_test)
    context = {
        'product': product
    }
    return render(request, 'accounts/single_product.html', context)


@login_required(login_url='login')
def createOrder(request, pk_test):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=pk_test)
    print(customer.id)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
        else:
            print("ERROR", formset.errors)
    context = {'formset': formset }
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
def updateOrder(request, pk_test):
    order = Order.objects.get(id=pk_test)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order) # instance=order argument is used to specify that the form should be pre-populated with the existing data of the order being updated. This allows the user to see the current values and make changes to them.
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form }
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk_test):
    order = Order.objects.get(id=pk_test)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order }
    return render(request, 'accounts/delete_order.html', context) 