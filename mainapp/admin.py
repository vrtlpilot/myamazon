from django.contrib import admin

# Register your models here.

from .models import ProductCategory, Product, Promo

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Promo)
