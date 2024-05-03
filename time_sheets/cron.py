from .models import TimeSheet
from config.settings import TELEGRAM_BOT_TOKEN, CHAT_ID
from django.utils import timezone
import requests
from django.contrib.auth import get_user_model

User = get_user_model

def send_time_sheet_reminder():
    now = timezone.now()
    today_date = now.date()

    users_with_chat_id = User.objects.filter(chat_id__gt=0, is_active=True)

    for user in users_with_chat_id:
        time_sheets_count = TimeSheet.objects.filter(
            user=user,
            date=today_date,
            time__gt=0
        ).count()

        if time_sheets_count == 0:
            message = f'Пожалуйста, {user.fullname()}, заполните отчет о рабочем времени за сегодня.'
            send_telegram_message(user.chat_id, message)

def send_telegram_message(chat_id, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=data)
    print(response.json())
