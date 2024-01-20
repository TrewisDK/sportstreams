# Generated by Django 4.1.4 on 2023-02-17 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0033_alter_translation_online'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranslationChatMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('room', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения чата',
            },
        ),
    ]