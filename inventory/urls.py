from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListCreate.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductRetrieve.as_view(), name='product-detail'),
    path('products/delete/<int:pk>/', views.ProductDelete.as_view(), name='product-delete'),
]