from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Message(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    text = models.TextField(verbose_name='Тело сообщения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время отправки сообщения')
