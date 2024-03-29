# Generated by Django 5.0 on 2024-01-09 08:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_shop_products_shop_in'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='اسم المصنع')),
                ('addr', models.TextField(blank=True, null=True, verbose_name='عنوان المصنع')),
                ('spic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.products', verbose_name='التخصص')),
            ],
        ),
    ]
