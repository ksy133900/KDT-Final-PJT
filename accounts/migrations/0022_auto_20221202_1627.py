# Generated by Django 3.2.12 on 2022-12-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_alter_profile_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='note_notice',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='notice_note',
            field=models.BooleanField(default=True),
        ),
    ]
