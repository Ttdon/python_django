# Generated by Django 2.1.5 on 2019-07-10 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20190704_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='ethnicity',
            name='flag',
            field=models.ImageField(blank=True, upload_to='ethnicity_flag'),
        ),
    ]