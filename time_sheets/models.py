from django.db import models

from tasks.models import Task
from django.contrib.auth import get_user_model

User = get_user_model()


class TimeSheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.FloatField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.task.task
