# Generated by Django 3.2.12 on 2022-12-06 07:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0009_alter_review_like_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='like_users',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]