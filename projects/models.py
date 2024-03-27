from django.db import models
from users.models import User
from clients.models import Client


class Status(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True)
    color = models.CharField(max_length=255, null=True)


class Project(models.Model):
    name = models.CharField(max_length=255)
    start_at = models.DateField(null=True)
    end_at = models.DateField(null=True)
    cost = models.FloatField(null=True, default=0)
    additional_info = models.TextField(null=True)
    status = models.ForeignKey(
        Status,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="project"
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True,
        related_name="projects"
    )
    banner = models.FileField(
        upload_to='media/projects/banners/',
        null=True, max_length=500
    )
    terms_of_reference = models.FileField(
        upload_to='media/projects/terms_of_reference/',
        null=True, max_length=500
    )
    agreement = models.FileField(
        upload_to='media/projects/agreement/',
        null=True, max_length=500
    )
    participants = models.ManyToManyField(User)

    def get_work_steps(self):
        return self.work_steps.all()


class WorkStep(models.Model):
    name = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='work_steps'
    )

    def __str__(self):
        return self.name
