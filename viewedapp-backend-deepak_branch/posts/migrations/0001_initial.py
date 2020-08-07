# Generated by Django 2.1.5 on 2019-09-09 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('about', models.TextField()),
                ('description', models.TextField()),
                ('is_18_plus', models.BooleanField(default=True)),
                ('link', models.CharField(blank=True, max_length=1000)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostMediaFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_media', to='posts.Post')),
            ],
        ),
    ]