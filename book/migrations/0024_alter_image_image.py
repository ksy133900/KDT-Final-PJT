# Generated by Django 3.2.12 on 2022-12-13 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0023_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default=0, upload_to='images/'),
        ),
    ]