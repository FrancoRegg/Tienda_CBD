from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductoSerializer, CategoriaSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriaSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductoSerializer
