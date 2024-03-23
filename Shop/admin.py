from django.contrib import admin
from .models import UserProfile, Products, ProductKeys, UserBuying, Rules, FAQ, Question

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Products)
admin.site.register(ProductKeys)
admin.site.register(UserBuying)
admin.site.register(Rules)
admin.site.register(FAQ)
admin.site.register(Question)
