# Generated by Django 4.1.3 on 2022-11-20 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0005_alter_cart_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(to='Ecommerce.products'),
        ),
    ]
