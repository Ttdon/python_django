# Generated by Django 2.1.5 on 2019-11-25 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0027_post_shared_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitionViewedByUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewed_comp_post', to='posts.Post')),
                ('viewed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewed_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='competitionviewedbyusers',
            unique_together={('post', 'viewed_by')},
        ),
    ]
