# Generated by Django 2.1.5 on 2019-07-04 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_user_views_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='views_count',
            new_name='profile_views_count',
        ),
    ]