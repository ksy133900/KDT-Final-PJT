# Generated by Django 3.2.12 on 2022-12-12 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_merge_0012_merge_20221212_1646_0014_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
