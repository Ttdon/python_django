# Generated by Django 2.1.5 on 2019-10-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_postmediafiles_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.ImageField(upload_to='images/post')),
            ],
        ),
    ]
