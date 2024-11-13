from django.urls import path
from pagos.views import *

urlpatterns = [
    path('pagos', pagos)
]