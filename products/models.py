from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)
from uuid import uuid4
import os

def UploadProduct(product, imageName):
    upload_to = 'products'
    ext = imageName.split('.')[-1]
    imageName = f'{uuid4().hex}.{ext}'
    return os.path.join(upload_to, imageName)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)
    subCategory = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    details = models.JSONField(default=list, blank=True)
    image = models.ImageField(upload_to=UploadProduct)

    def __str__(self) -> str:
        return self.name
