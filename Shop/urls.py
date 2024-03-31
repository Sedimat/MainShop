from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", LoginView.as_view(), name='login'),
    path("logout", views.logout_view, name='logout'),
    path("registration", views.registration, name='registration'),
    path("product/<int:id>", views.product, name="product"),
    path("buy/<int:id>", views.buy, name="buy"),
    path("user", views.user, name='user'),
    path("news", views.news, name='news'),
    path("new/<int:id>", views.new, name="new"),
    path("shop", views.shop, name='shop'),
    path("mode", views.mode, name='mode'),
    path("mod/<int:id>", views.mod, name='mod'),
    path("support", views.support, name='support'),
    path("rules", views.rules, name='rules'),
    path("src", views.src, name='src'),


]