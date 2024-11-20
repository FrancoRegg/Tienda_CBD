from django.urls import path
from apps.productos.views import productos

urlpatterns = [
    path('productos', productos)
]