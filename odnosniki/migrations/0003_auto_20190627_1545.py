# Generated by Django 2.2 on 2019-06-27 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odnosniki', '0002_auto_20190620_2100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='odnosnik',
            old_name='name',
            new_name='nazwa',
        ),
        migrations.RenameField(
            model_name='odnosnik',
            old_name='image',
            new_name='zdjecie',
        ),
    ]
