from django.contrib import admin
from .models import UserProfile, Products, ProductKeys, UserBuying

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Products)
admin.site.register(ProductKeys)
admin.site.register(UserBuying)
