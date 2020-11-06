from rest_framework import routers

from chat.views import ConversationViewSet, ChatViewSet


conversation_router = routers.SimpleRouter()
conversation_router.register(r"conversations", ConversationViewSet)

chat_router = routers.SimpleRouter()
chat_router.register(r"chats", ChatViewSet)
