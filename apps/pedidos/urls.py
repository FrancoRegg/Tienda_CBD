from django.urls import path
from apps.pedidos.views import *

urlpatterns = [
    path('pedidos', pedidos)
]