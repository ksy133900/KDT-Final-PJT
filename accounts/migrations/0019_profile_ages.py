# Generated by Django 3.2.12 on 2022-12-01 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20221130_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ages',
            field=models.CharField(choices=[('', ''), ('20대', '20대'), ('30대', '30대'), ('40대', '40대'), ('50대', '50대')], default='장르', max_length=20),
        ),
    ]