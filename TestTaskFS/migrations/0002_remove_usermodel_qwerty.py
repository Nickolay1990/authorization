# Generated by Django 4.2.1 on 2023-05-28 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestTaskFS', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='qwerty',
        ),
    ]
