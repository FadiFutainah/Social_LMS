# Generated by Django 4.0.4 on 2022-07-06 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='membership',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
    ]
