# Generated by Django 4.2.5 on 2023-09-27 10:24

from django.db import migrations, models
import django.db.models.deletion
import users.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('date_joined', models.DateField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('github', models.CharField(max_length=255, null=True)),
                ('linkedin', models.CharField(max_length=255, null=True)),
                ('telegram', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('salary', models.FloatField()),
                ('hourly_payment_cost', models.FloatField()),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to='users.position')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', users.managers.CustomUserManager()),
            ],
        ),
    ]
