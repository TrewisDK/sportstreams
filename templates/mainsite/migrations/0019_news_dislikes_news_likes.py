# Generated by Django 4.1.4 on 2022-12-28 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0018_news_photo_author_alter_news_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]