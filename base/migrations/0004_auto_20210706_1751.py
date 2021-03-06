# Generated by Django 3.1.6 on 2021-07-06 12:21

import django.contrib.auth.password_validation
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['tid']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['uid']},
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100, validators=[django.contrib.auth.password_validation.validate_password]),
        ),
    ]
