# Generated by Django 3.0.4 on 2022-01-24 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_order_orderdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]