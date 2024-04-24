from .models import TimeSheet
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def my_scheduled_job():
    subject = 'Test Cron'
    message = 'Hello I\'m Upwards'
    email_from = EMAIL_HOST_USER
    recipient_list = ['zulpukarovmarsel17@gmail.com']

    send_mail(subject, message, email_from, recipient_list)
