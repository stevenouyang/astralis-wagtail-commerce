# Generated by Django 5.0.1 on 2024-02-29 15:36

import autoslug.fields
import django.db.models.manager
import store.utils.fileupload
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('image', models.ImageField(blank=True, null=True, upload_to=store.utils.fileupload.category_image_upload_path)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
            managers=[
                ('everything', django.db.models.manager.Manager()),
            ],
        ),
    ]
