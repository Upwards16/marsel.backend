# Generated by Django 4.2.5 on 2023-10-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_remove_lead_source_lead_traffic_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='reminder_date',
            field=models.DateTimeField(),
        ),
    ]
