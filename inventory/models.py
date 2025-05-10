from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    ingredients = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    
    def __str__(self):
        return self.name