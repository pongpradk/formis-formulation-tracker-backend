from django.db.models.signals import post_save # post_save is a signal that is sent when a Product model is saved
from django.dispatch import receiver
import re
from .models import Product, Ingredient

def is_valid_ingredient(text):
    return len(text) >= 2 and re.search('[a-zA-Z]', text)

def extract_valid_ingredients(ingredients_text):
    if not ingredients_text:
        return []
        
    raw_parts = [part.strip() for part in ingredients_text.split(',')]
    
    valid_ingredients = []
    current_part = ""
    
    for part in raw_parts:
        if not current_part:
            current_part = part
        else:
            current_part = current_part + "," + part
        
        if is_valid_ingredient(current_part):
            valid_ingredients.append(current_part)
            current_part = ""
    
    if current_part and is_valid_ingredient(current_part):
        valid_ingredients.append(current_part)
        
    return valid_ingredients

@receiver(post_save, sender=Product) # indicates this function is a signal receiver
def process_product_ingredients(sender, instance, created, **kwargs): # instance = Product, created = True if new Product else False
    Ingredient.objects.filter(product=instance).delete()
    
    # Get valid ingredients
    valid_ingredients = extract_valid_ingredients(instance.ingredients)
    
    ingredient_objects = []
    for position, name in enumerate(valid_ingredients):
        ingredient_objects.append(Ingredient(
            product=instance,
            name=name,
            position=position
        ))
    
    if ingredient_objects:
        Ingredient.objects.bulk_create(ingredient_objects)