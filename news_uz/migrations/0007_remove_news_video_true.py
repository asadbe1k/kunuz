# Generated by Django 5.1.1 on 2024-11-18 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_uz', '0006_alter_news_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='video_true',
        ),
    ]
