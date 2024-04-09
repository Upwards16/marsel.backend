from django.db import models
from users.models import User

class ClientStatus(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class TrafficSource(models.Model):
    name = models.CharField(max_length=255)


class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.DateField(null=True)
    comment = models.TextField(null=True)
    status = models.ForeignKey(
        ClientStatus, on_delete=models.SET_NULL,
        null=True
    )
    manager = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="client"
    )
    traffic_source = models.ForeignKey(
        TrafficSource,
        null=True,
        on_delete=models.SET_NULL,
        related_name="client_traffic"
    )

    def get_all_projects(self):
        return self.projects.all()
