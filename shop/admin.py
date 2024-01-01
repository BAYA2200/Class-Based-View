from django.contrib import admin

# Register your models here.
from shop.models import Product, Firm, Category

admin.site.register(Product)
admin.site.register(Firm)
admin.site.register(Category)