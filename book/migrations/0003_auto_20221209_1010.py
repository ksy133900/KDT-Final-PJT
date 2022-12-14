# Generated by Django 3.2.12 on 2022-12-09 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
    ]
