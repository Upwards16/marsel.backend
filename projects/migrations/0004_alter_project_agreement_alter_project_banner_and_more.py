# Generated by Django 4.2.5 on 2023-10-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='agreement',
            field=models.FileField(max_length=500, null=True, upload_to='media/projects/agreement/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='banner',
            field=models.FileField(max_length=500, null=True, upload_to='media/projects/banners/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='terms_of_reference',
            field=models.FileField(max_length=500, null=True, upload_to='media/projects/terms_of_reference/'),
        ),
    ]
