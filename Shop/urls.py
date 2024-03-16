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
]