from django.contrib import admin
from .models import UserProfile, Products, ProductKeys, UserBuying, Rules, FAQ, Question, ModeQuestion, RareQuestion, \
    Mode, News

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Products)
admin.site.register(ProductKeys)
admin.site.register(UserBuying)
admin.site.register(Rules)
admin.site.register(FAQ)
admin.site.register(Question)
admin.site.register(ModeQuestion)
admin.site.register(RareQuestion)
admin.site.register(Mode)
admin.site.register(News)

