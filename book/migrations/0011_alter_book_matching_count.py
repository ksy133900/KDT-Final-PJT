# Generated by Django 3.2.12 on 2022-12-12 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='matching_count',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
