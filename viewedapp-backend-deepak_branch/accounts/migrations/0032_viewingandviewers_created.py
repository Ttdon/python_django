# Generated by Django 2.1.5 on 2019-08-09 07:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20190718_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewingandviewers',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]