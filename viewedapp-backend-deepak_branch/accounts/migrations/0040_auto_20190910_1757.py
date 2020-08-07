# Generated by Django 2.1.5 on 2019-09-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_auto_20190826_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_post_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='post_counts',
            field=models.IntegerField(default=0),
        ),
    ]
