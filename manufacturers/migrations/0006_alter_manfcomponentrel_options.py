# Generated by Django 5.0 on 2024-03-05 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturers', '0005_remove_manfcomponentrel_howmany'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manfcomponentrel',
            options={'permissions': [('can_give_perm', 'صلاحية تغير المرحلة')], 'verbose_name': 'قطعة للتصنيع', 'verbose_name_plural': 'المصنع'},
        ),
    ]
