# Generated by Django 5.0 on 2024-02-28 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0004_delete_customuser_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
    ]
