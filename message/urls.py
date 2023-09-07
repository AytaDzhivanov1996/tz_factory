from django.urls import path

from message.views import MessageCreateAPIView, MessageListApiView

urlpatterns = [
    path('create_message/', MessageCreateAPIView.as_view()),
    path('list_message/', MessageListApiView.as_view())
]