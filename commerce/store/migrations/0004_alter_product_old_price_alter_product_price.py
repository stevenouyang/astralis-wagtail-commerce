# Generated by Django 5.0.1 on 2024-03-01 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_old_price_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(decimal_places=2, default='69069.00', max_digits=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default='69000.00', max_digits=15),
        ),
    ]
