# from .models import TimeSheet
# from config.settings import EMAIL_HOST_USER
# from django.core.mail import send_mail
# from datetime import datetime, timedelta
#
#
# def send_time_sheet_reminder():
#     now = datetime.now()
#     today_date = now.date()
#
#     time_sheets_count = TimeSheet.objects.filter(
#         user__is_active=True,
#         date=today_date,
#         time__gt=0
#     ).count()
#
#     if time_sheets_count == 0:
#         subject = 'Напоминание: заполните отчет о рабочем времени'
#         message = 'Пожалуйста, заполните отчет о рабочем времени за сегодня.'
#         email_from = EMAIL_HOST_USER
#         recipient_list = ['zulpukarovmarsel17@gmail.com']
#
#         send_mail(subject, message, email_from, recipient_list)

from .models import TimeSheet
from config.settings import TELEGRAM_BOT_TOKEN, CHAT_ID
from django.utils import timezone
import requests


def send_time_sheet_reminder():
    now = timezone.now()
    today_date = now.date()

    time_sheets_count = TimeSheet.objects.filter(
        user__is_active=True,
        date=today_date,
        time__gt=0
    ).count()

    if time_sheets_count == 0:
        message = 'Пожалуйста, заполните отчет о рабочем времени за сегодня.'
        send_telegram_message(message)


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=data)
    print(response.json())
