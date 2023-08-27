from django.contrib import admin
from .models import (
    Profile,
    Address
)

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'avtar', 'address')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'pincode', 'city', 'address')


admin.site.register(Address, AddressAdmin)
admin.site.register(Profile, ProfileAdmin)