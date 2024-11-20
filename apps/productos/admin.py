from django.contrib import admin

# Register your models here.
from apps.productos.models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductReview)
admin.site.register(Discount)
admin.site.register(ProductDiscount)
admin.site.register(ProductImage)