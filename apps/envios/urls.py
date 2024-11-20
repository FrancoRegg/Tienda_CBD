from django.urls import path
from apps.envios.views import *

urlpatterns = [
    path('envios', envios)
]