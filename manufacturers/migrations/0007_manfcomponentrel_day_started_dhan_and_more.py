# Generated by Django 5.0 on 2024-03-08 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturers', '0006_alter_manfcomponentrel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='manfcomponentrel',
            name='day_started_dhan',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manfcomponentrel',
            name='day_started_manf',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manfcomponentrel',
            name='day_started_tshted',
            field=models.DateField(blank=True, null=True),
        ),
    ]
