# Generated by Django 2.1.5 on 2019-06-18 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190618_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sociallink',
            name='link',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]