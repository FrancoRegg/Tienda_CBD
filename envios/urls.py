from django.urls import path
from envios.views import *

urlpatterns = [
    path('envios', envios)
]