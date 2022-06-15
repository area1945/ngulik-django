from rest_framework import serializers
from .models import CartItem
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=64, required=True)
    email = serializers.CharField(max_length=64, required=True)
    phone = serializers.CharField(max_length=64, required=True)
    website = serializers.CharField(max_length=64, required=False)
    address = serializers.CharField(required=True)

    class Meta:
        model = Contact
        fields = ('__all__')

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CartItem
        fields = ('__all__')