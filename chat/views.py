from chat.models import Chat, Conversation
from chat.serializers import ChatSerializer, ConversationSerializer
from rest_framework import viewsets


class ConversationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing Conversation instances.
    """

    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()


class ChatViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Chat instances.
    """

    serializer_class = ChatSerializer
    queryset = Chat.objects.all()
