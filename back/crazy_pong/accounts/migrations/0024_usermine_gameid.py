# Generated by Django 3.2.10 on 2024-01-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_merge_20240115_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermine',
            name='gameId',
            field=models.CharField(default='', max_length=128),
        ),
    ]