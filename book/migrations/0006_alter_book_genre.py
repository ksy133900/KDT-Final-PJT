# Generated by Django 3.2.12 on 2022-12-09 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_merge_0004_auto_20221209_1027_0004_auto_20221209_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
