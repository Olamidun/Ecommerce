# Generated by Django 3.0.6 on 2020-06-03 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0007_cart_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.Cart'),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='line_total',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, related_name='item_cart', to='carts.CartItems'),
        ),
    ]
