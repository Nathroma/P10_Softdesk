# Generated by Django 3.2.5 on 2021-08-25 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_projects', '0002_remove_project_project_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author_user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='assignee_user',
            new_name='assignee',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='author_user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='author_user_id',
            new_name='author',
        ),
    ]
