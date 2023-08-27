from django.contrib import admin
from .models import (
    Category,
    Product
)

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subCategory')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'discount', 'details')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)