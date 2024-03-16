# Generated by Django 5.0.3 on 2024-03-16 15:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_products_userprofile_wallet_productkeys'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productkeys',
            options={'verbose_name': 'Ключ Товару', 'verbose_name_plural': 'Ключі Товару'},
        ),
        migrations.CreateModel(
            name='UserBuying',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keys', models.CharField(max_length=100, verbose_name='Ключ')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна товару')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.products', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Покупка користувача',
                'verbose_name_plural': 'Покупки користувача',
            },
        ),
    ]