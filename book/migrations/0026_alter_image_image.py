# Generated by Django 3.2.12 on 2022-12-13 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0025_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default='images/dummy-image-square.jpg', upload_to='images/'),
        ),
    ]
