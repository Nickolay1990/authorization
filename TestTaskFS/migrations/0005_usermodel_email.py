# Generated by Django 4.2.1 on 2023-05-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestTaskFS', '0004_alter_usermodel_name_alter_usermodel_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
