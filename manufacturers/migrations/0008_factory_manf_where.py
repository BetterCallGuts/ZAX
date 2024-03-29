# Generated by Django 5.0 on 2024-03-08 23:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturers', '0007_manfcomponentrel_day_started_dhan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='اسم المصنع')),
                ('addr', models.TextField(blank=True, null=True, verbose_name='عنوان المصنع')),
            ],
            options={
                'verbose_name': 'مصنع',
                'verbose_name_plural': 'المصانع',
            },
        ),
        migrations.AddField(
            model_name='manf',
            name='where',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manufacturers.factory', verbose_name='المصنع'),
        ),
    ]
