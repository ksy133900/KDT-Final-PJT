# Generated by Django 3.2.12 on 2022-12-13 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0032_alter_book_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='grade',
        ),
    ]