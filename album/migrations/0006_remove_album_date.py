# Generated by Django 3.0.8 on 2020-07-20 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_auto_20200719_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='date',
        ),
    ]
