# Generated by Django 3.0.4 on 2020-06-23 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_album_publish_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='genre',
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]