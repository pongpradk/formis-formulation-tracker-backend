from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import ProductSerializer, IngredientSerializer
from .models import Product, Ingredient
from rest_framework.permissions import IsAuthenticated

class ProductListCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductDelete(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)

class ProductRetrieve(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)

class ProductUpdate(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)

class IngredientList(generics.ListAPIView):
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id, owner=self.request.user)
        return Ingredient.objects.filter(product=product)
