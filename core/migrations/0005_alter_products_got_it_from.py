# Generated by Django 4.2.7 on 2023-12-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_sales_what_got_saled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='got_it_from',
            field=models.CharField(blank=True, choices=[], max_length=255, null=True, verbose_name='تم شرائه من'),
        ),
    ]
