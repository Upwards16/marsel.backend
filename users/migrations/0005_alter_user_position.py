# Generated by Django 4.2.5 on 2023-09-27 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_hourly_payment_cost_alter_user_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to='users.position'),
        ),
    ]
