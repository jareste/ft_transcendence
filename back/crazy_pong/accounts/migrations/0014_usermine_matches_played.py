# Generated by Django 3.2.10 on 2023-12-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20231230_1359'),
        ('accounts', '0013_remove_usermine_matches_played'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermine',
            name='matches_played',
            field=models.ManyToManyField(blank=True, to='game.Match'),
        ),
    ]
