# Generated by Django 3.2 on 2022-05-15 16:16

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('roombook', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='booking',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
