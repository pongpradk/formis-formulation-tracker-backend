from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'ingredients', 'manufacturing_date', 'expiration_date', 'owner']
        extra_kwargs = {'owner': {'read_only': True}}