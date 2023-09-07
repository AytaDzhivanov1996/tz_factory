from rest_framework.generics import CreateAPIView, ListAPIView

from message.models import Message
from message.serializers import MessageSerializer
from message.telegram import send_message

class MessageCreateAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        send_message(self.request.data.get('text'), self.request.data.get('chat_id'))


class MessageListApiView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(user=self.request.user)
