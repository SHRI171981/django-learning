from django.forms import ModelForm
from .models import Order, Product, Customer

class OrderForm(ModelForm):
    class Meta:
        model = Order # specifies the model that the form is based on.
        fields = '__all__' # specifies that all fields of the model should be included in the form. Alternatively, you can specify a list of fields to include, e.g., fields = ['customer', 'product', 'status'].
        