# Generated by Django 5.0.3 on 2024-03-23 15:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_faq_rules_products_number_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='datetime',
        ),
        migrations.AddField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
