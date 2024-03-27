from django.db import models
from projects.models import Project
from django.contrib.auth import get_user_model

User = get_user_model()


class Mark(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Column(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        related_name="tasks"
    )
    column = models.ForeignKey(
        Column,
        on_delete=models.SET_NULL,
        null=True
    )
    task = models.TextField()
    deadline = models.DateTimeField()
    mark = models.ForeignKey(
        Mark, on_delete=models.SET_NULL,
        related_name="tasks",
        null=True
    )
    participants = models.ManyToManyField(
        User,
        related_name="tasks",
        blank=True
    )
    attachment = models.FileField(
        upload_to="media/tasks/attachment/",
        null=True,
        max_length=500
    )
    description = models.TextField(null=True)
    position = models.IntegerField(null=True, default=1)

    def __str__(self):
        return self.task

