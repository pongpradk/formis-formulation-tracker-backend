from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    ingredients = models.TextField()
    manufacturing_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ingredient_items')
    name = models.CharField(max_length=200)
    position = models.PositiveIntegerField()  # Using 0-based indexing
    
    class Meta:
        ordering = ['position']  # Default ordering by position
        unique_together = ['product', 'position']  # Prevent duplicate positions
    
    def __str__(self):
        return f"{self.name} (#{self.position+1})"