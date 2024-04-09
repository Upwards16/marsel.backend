from django.contrib import admin
from .models import PaymentType, ExpenseType, Expense, Income
# Register your models here.


admin.site.register(PaymentType)
admin.site.register(Expense)
admin.site.register(ExpenseType)
admin.site.register(Income)