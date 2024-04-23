from django.utils import timezone
from config.settings import TELEGRAM_BOT_TOKEN, CHAT_ID, EMAIL_HOST_USER
from .models import Lead
from config.celery import app
from django.core.mail import send_mail
import requests

@app.task
def send_reminder_notification_to_email(lead_id):
    from .models import Lead

    lead = Lead.objects.get(id=lead_id)

    reminder_time = lead.reminder_date
    current_time = timezone.now()
    time_difference = reminder_time - current_time
    if time_difference.total_seconds() <= 10800:
        subject = 'Напоминание о звонке'
        message = f'Привет!\nНапоминаю вам о нашем сегодняшнем звонке. До него осталось 3 часа. Пожалуйста, не забудьте о нем.'
        email_from = EMAIL_HOST_USER
        recipient_list = [lead.user.email]
        send_mail(subject, message, email_from, recipient_list)
@app.task
def send_reminder_notification_to_telegram(lead_id):
    lead = Lead.objects.get(id=lead_id)

    reminder_time = lead.reminder_date
    current_time = timezone.now()
    time_difference = reminder_time - current_time
    if time_difference.total_seconds() <= 10800:
        message = f'Привет!\nНапоминаю вам о нашем сегодняшнем звонке. До него осталось 3 часа. Пожалуйста, не забудьте о нем.'
        send_telegram_message(message)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    response = requests.get(url)
    print(response.json())
