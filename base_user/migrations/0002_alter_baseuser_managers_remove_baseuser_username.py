# Generated by Django 5.1.2 on 2024-10-26 04:42

import base_user.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='baseuser',
            managers=[
                ('objects', base_user.models.CUserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='baseuser',
            name='username',
        ),
    ]