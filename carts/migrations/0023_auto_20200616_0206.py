# Generated by Django 3.0.6 on 2020-06-16 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0022_auto_20200616_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='billing_address',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='carts.BillingAddress'),
        ),
    ]