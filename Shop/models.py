from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    avatar = models.ImageField(upload_to='avatar', default='avatar/avatar_crj2ayQ.jpg')
    description = models.TextField(blank=True, verbose_name="Опис")
    wallet = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name="Гаманець")

    def __str__(self):
        return f'Додаткова інформація: {self.id_user}'

    class Meta:
        verbose_name = "Користувач додаток"
        verbose_name_plural = "Користувачі додаток"



class Products(models.Model):
    name = models.CharField(max_length=50, verbose_name="Назва")
    img = models.ImageField(upload_to='avatar', default='product/avatar_crj2ayQ.jpg')
    description = models.TextField(blank=True, verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна товару")
    discont = models.DecimalField(max_digits=100, decimal_places=0, verbose_name="Знижка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"

class ProductKeys(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="Товар")
    keys = models.TextField(blank=True, verbose_name="Ключ")

    def __str__(self):
        return f'Ключі: {self.product}'

    class Meta:
        verbose_name = "Ключ Товару"
        verbose_name_plural = "Ключі Товару"

class UserBuying(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="Товар")
    keys = models.CharField(max_length=100, verbose_name="Ключ")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна товару")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Покупка: {self.id_user}'

    class Meta:
        verbose_name = "Покупка користувача"
        verbose_name_plural = "Покупки користувача"