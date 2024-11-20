from django.urls import path
from apps.pagos.views import *

urlpatterns = [
    path('pagos', pagos)
]