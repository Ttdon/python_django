# Generated by Django 2.1.5 on 2019-09-09 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('1', 'Text'), ('2', 'Image'), ('3', 'Video'), ('4', 'Audio'), ('5', 'Poll'), ('6', 'Competition')], default='1', max_length=20),
            preserve_default=False,
        ),
    ]