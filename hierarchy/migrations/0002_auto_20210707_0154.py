# Generated by Django 3.1.6 on 2021-07-06 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'ordering': ['si_no']},
        ),
        migrations.RenameField(
            model_name='table',
            old_name='Parent_ID',
            new_name='parent_id',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='SI_No',
            new_name='si_no',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='Title',
            new_name='title',
        ),
    ]
