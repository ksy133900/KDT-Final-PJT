# Generated by Django 3.2.12 on 2022-12-14 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0039_auto_20221214_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
