# Generated by Django 4.2.5 on 2023-11-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_status_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='color',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
