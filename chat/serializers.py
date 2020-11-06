from rest_framework import serializers

from chat.models import Conversation, Chat


def to_backend(dikt):
    mappings = [
        ("conversationId", "conversation"),
        ("userId", "user"),
    ]
    for fe_key, be_key in mappings:
        dikt[be_key] = dikt.pop(fe_key)
    return dikt


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [
            "conversation",
            "payload",
            "user",
        ]

    def __init__(self, *args, **kwargs):
        if "data" in kwargs:
            kwargs["data"].update(**kwargs["data"].pop("chat"))
            kwargs["data"] = to_backend(kwargs["data"])
        super().__init__(*args, **kwargs)


class NestedChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [
            "payload",
            "userId",
            "utc-date",
            "status",
        ]
        extra_kwargs = {
            "userId": {"source": "user_id"},
            "utc-date": {"source": "created_at"}
        }


class ConversationSerializer(serializers.ModelSerializer):

    operatorGroup = serializers.SerializerMethodField()

    chats = NestedChatSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = [
            "conversationId",
            "storeId",
            "operatorId",
            "clientId",
            "operatorGroup",
            "chats",
        ]
        extra_kwargs = {
            "conversationId": {"source": "id"},
            "storeId": {"source": "store_id"},
            "operatorId": {"source": "operator_id"},
            "clientId": {"source": "client_id"},
        }

    def get_operatorGroup(self, obj):
        return obj.operator.group.name
