# Generated by Django 3.0.6 on 2020-06-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0013_cartitems_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
