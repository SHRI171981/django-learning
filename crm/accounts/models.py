from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True) # automatically set the field to now when the object is first created.

    def __str__(self):
        return self.name
    

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length=255, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY) # choices is used to limit the options for the field to a predefined set of values.

    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    # # TO BE CONTINUED IN THE NEXT VIDEO
    # customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    # product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS) # choices is used to limit the options for the field to a predefined set of values.    

