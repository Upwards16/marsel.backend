# Generated by Django 4.2.5 on 2023-10-27 08:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_alter_task_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
