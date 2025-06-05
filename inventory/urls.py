from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListCreate.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductRetrieve.as_view(), name='product-detail'),
    path('products/update/<int:pk>/', views.ProductUpdate.as_view(), name='product-update'),
    path('products/delete/<int:pk>/', views.ProductDelete.as_view(), name='product-delete'),
    path('products/<int:product_id>/ingredients/', views.IngredientList.as_view(), name='ingredient-list'),
    path('products/<int:product_id>/compare-ingredients/', views.IngredientCompareView.as_view(), name='compare-ingredients'),
]