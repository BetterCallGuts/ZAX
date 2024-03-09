# Generated by Django 5.0 on 2024-03-08 23:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_products_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='shopin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.shop', verbose_name='يعرض في محل'),
        ),
    ]