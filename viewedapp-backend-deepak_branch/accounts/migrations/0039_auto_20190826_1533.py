# Generated by Django 2.1.5 on 2019-08-26 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_removefromsuggestionsrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileviewsrecoard',
            name='profile_viewed_by',
        ),
        migrations.RemoveField(
            model_name='profileviewsrecoard',
            name='profile_viewed_to',
        ),
        migrations.DeleteModel(
            name='ProfileViewsRecoard',
        ),
    ]
