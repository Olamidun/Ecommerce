# Generated by Django 3.0.6 on 2020-06-16 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0021_auto_20200616_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carts.BillingAddress'),
        ),
    ]