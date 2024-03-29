# Generated by Django 5.0 on 2024-03-04 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturers', '0003_alter_manfcomponentrel_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManfComponentRelHowManyComp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_many', models.IntegerField(default=1)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturers.components')),
            ],
        ),
        migrations.AlterField(
            model_name='manfcomponentrel',
            name='component',
            field=models.ManyToManyField(blank=True, to='manufacturers.manfcomponentrelhowmanycomp', verbose_name='القطع'),
        ),
    ]
