# Generated by Django 3.2.12 on 2022-12-12 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0021_review_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='genre',
        ),
    ]
