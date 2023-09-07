import requests
from django.conf import settings
from rest_framework.response import Response


def send_message(text, chat_id):
    data_for_request = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.get(f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage',
                            data_for_request)
    return Response(response.json())
