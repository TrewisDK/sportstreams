# Generated by Django 4.1.4 on 2022-12-29 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0019_news_dislikes_news_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='description',
            field=models.TextField(default='Прямая трансляция', max_length=3000),
        ),
    ]