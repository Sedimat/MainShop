# Generated by Django 5.0.3 on 2024-03-23 15:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_alter_productkeys_options_userbuying'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('question', models.TextField(blank=True, verbose_name='Питання')),
                ('answer', models.TextField(blank=True, verbose_name='Відповідь')),
            ],
            options={
                'verbose_name': 'Поширене запитання',
                'verbose_name_plural': 'Поширені запитання',
            },
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Правило',
                'verbose_name_plural': 'Правила',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='number',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Проданих'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, verbose_name='Питання')),
                ('datetime', models.CharField(max_length=100, verbose_name='Дата')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Запитання',
                'verbose_name_plural': 'Запитання',
            },
        ),
    ]
