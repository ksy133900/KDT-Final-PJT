# Generated by Django 3.2.12 on 2022-12-08 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_user_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=8, null=True, unique=True),
        ),
    ]
