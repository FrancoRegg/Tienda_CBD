from django.urls import path
from productos.views import prueba_ruta

urlpatterns = [
    path('productos', prueba_ruta)
]