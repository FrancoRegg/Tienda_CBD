from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories')

class Product(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=False, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, through='ProductCategory')
    created_at = models.DateTimeField(auto_now_add=True)

class ProductCategory(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('usuarios.User', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Discount(models.Model):
    name = models.CharField(max_length=100)
    discount_type = models.CharField(max_length=20, choices=[('percentage', 'Percentage'), ('fixed', 'Fixed Amount')])
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class ProductDiscount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField()
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
