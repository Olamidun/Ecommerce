# Generated by Django 3.0.6 on 2020-06-10 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0011_auto_20200607_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, related_name='item_cart', to='carts.CartItems'),
        ),
    ]
