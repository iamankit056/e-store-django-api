from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import os

# Create your models here.
def UploadAvtar(profile, imageName):
    upload_to = 'avtars'
    ext = imageName.split('.')[-1]
    imageName = f'{uuid4().hex}.{ext}'
    return os.path.join(upload_to, imageName)


class Address(models.Model):
    state = models.CharField(max_length=128, blank=True, null=True)
    pincode = models.CharField(max_length=8, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    address = models.TextField(blank=True, null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avtar = models.ImageField(default='avtars/default.png', upload_to=UploadAvtar)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)