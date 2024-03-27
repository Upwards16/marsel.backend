from django.db import models
from projects.models import Project


class PaymentType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Income(models.Model):
    act_number = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.FloatField()
    account_number = models.CharField(max_length=255)
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL,
        related_name="incomes",
        null=True
    )
    payment_type = models.ForeignKey(
        PaymentType, on_delete=models.SET_NULL,
        related_name="incomes",
        null=True
    )
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.act_number


class ExpenseType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    expense_type = models.ForeignKey(
        ExpenseType, on_delete=models.SET_NULL,
        null=True
    )
    date = models.DateField()
    amount = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    attachment = models.FileField(
        upload_to="media/cash/expenses/attachments/",
        null=True,
        max_length=500
    )

