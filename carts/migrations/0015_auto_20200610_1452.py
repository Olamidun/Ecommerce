# Generated by Django 3.0.6 on 2020-06-10 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0014_auto_20200610_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitems',
            old_name='product',
            new_name='items',
        ),
    ]
