import django_filters
from django_filters import DateFilter, CharFilter
from .models import Customer, Product, Order

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'product', 'status']
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')
    note = CharFilter(field_name='note', lookup_expr='icontains')
    # product = CharFilter(field_name='product', lookup_expr='icontains') # cannot filter by foreign key
