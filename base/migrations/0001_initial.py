# Generated by Django 3.1.6 on 2021-07-06 04:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Please Ensure that username follows the convention', regex='^[a/A][a-zA-Z0-9]*[1/0]$')])),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('task_title', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(4)])),
                ('task_description', models.TextField(max_length=2000, null=True)),
                ('task_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.user')),
            ],
        ),
    ]
