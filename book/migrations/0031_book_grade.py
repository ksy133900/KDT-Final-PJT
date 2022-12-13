# Generated by Django 3.2.12 on 2022-12-13 08:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0030_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='grade',
            field=models.IntegerField(default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
