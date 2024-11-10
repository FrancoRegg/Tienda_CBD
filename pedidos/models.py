from django.db import models
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('usuarios.User', on_delete=models.CASCADE)
    shipping_address = models.ForeignKey('usuarios.Address', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, default='Pending')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now, auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('productos.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class OrderTracking(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    tracking_number = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now, auto_now=True)
    notes = models.TextField(blank=True, null=True)

class Cart(models.Model):
    user = models.ForeignKey('usuarios.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('productos.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added_at = models.DateTimeField(default=timezone.now, auto_now_add=True)

class InventoryTransaction(models.Model):
    product = models.ForeignKey('productos.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_type = models.CharField(max_length=50)
    transaction_date = models.DateTimeField(default=timezone.now, auto_now_add=True)
    reference_order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)