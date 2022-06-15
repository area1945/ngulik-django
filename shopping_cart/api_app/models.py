from django.db import models

# Create your models here.
class CartItem(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()

class Contact(models.Model):
    name = models.CharField(max_length=64, default=None, blank=True, null=True)
    email = models.CharField(max_length=64, default=None, blank=True, null=True)
    phone = models.CharField(max_length=64, default=None, blank=True, null=True)
    website = models.CharField(max_length=64, default=None, blank=True, null=True)
    address = models.TextField(default=None, blank=True, null=True)