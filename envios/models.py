from django.db import models

# Create your models here.
class Shipping (models.Model):
    order = models.ForeignKey('pedidos.Order', on_delete=models.CASCADE)
    address = models.ForeignKey('usuarios.Address', on_delete=models.CASCADE)
    shipping_date = models.DateTimeField()