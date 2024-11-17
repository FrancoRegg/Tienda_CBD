from django.contrib import admin

# Register your models here.
from pedidos.models import *

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderTracking)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(InventoryTransaction)