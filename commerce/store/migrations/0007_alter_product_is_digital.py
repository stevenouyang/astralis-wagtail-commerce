# Generated by Django 5.0.1 on 2024-03-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_spectable_remove_product_specification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_digital',
            field=models.BooleanField(default=False),
        ),
    ]
