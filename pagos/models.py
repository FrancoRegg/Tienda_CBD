from django.db import models

# Create your models here.
class Payment(models.Model):
    order = models.ForeignKey('pedidos.Order', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Completed')