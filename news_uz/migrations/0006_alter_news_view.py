# Generated by Django 5.1.1 on 2024-11-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_uz', '0005_alter_news_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='view',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
