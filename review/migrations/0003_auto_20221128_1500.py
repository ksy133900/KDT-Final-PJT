# Generated by Django 3.2.12 on 2022-11-28 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_alter_review_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='genre',
            field=models.CharField(choices=[('추리', '추리'), ('스릴러', '스릴러'), ('공포', '공포'), ('판타지', '판타지'), ('로맨스', '로맨스')], max_length=20, null=True),
        ),
    ]
