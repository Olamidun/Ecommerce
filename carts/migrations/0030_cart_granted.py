# Generated by Django 3.0.6 on 2020-07-20 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0029_auto_20200720_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='granted',
            field=models.BooleanField(default=False),
        ),
    ]
