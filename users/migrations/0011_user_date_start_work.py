# Generated by Django 4.2.5 on 2023-10-04 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_rename_date_of_joined_user_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_start_work',
            field=models.DateField(blank=True, null=True),
        ),
    ]
