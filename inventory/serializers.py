from .models import Product, Ingredient
from rest_framework import serializers

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'position']
        # We don't include product in fields because it will be set from the URL

class ProductSerializer(serializers.ModelSerializer):
    ingredient_items = IngredientSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'ingredients', 'manufacturing_date', 'expiration_date', 'owner', 'ingredient_items']
        extra_kwargs = {'owner': {'read_only': True}}