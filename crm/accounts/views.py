from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the CRM Home Page!")


def products(request):
    return HttpResponse("This is the products page.")


def customers(request):
    return HttpResponse("This is the customers page.")