from django.utils.dateparse import parse_datetime
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

from chat.models import (
    Store,
    OperatorGroup,
    Operator,
    Conversation,
    Chat,
)
User = get_user_model()


class Command(BaseCommand):
    help = "Create conversation if it doesn't exist"

    @transaction.atomic
    def handle(self, *args, **options):
        if Conversation.objects.exists():
            self.stdout.write(
                self.style.SUCCESS("Conversation already exists")
            )
            return
        store = Store.objects.create()
        user = User.objects.create(username="johndoe")
        operator_group = OperatorGroup.objects.create(name="sales")
        operator = Operator.objects.create(group=operator_group)
        conversation = Conversation.objects.create(
            store=store,
            client_id=123,
            operator=operator,
            discount_code="abc123",
        )

        chats = [
            {
                "payload": "Hello. This is {{ operator.Name }}.\nHow can I help you?",
                "user_id": user.pk,
                "utc-date": "2020-10-01T12:15:30-05:00",
                "status": "sent",
            },
            {
                "payload": (
                    "Hi Emma this is Mark. I want to make a purchase of around"
                    " 1000$ in products. Is there any discount available?"
                ),
                "user_id": user.pk,
                "utc-date": "2020-10-01T12:15:31-02:41",
                "status": "sent",
            },
            {
                "payload": "Sure {{ username }}. Here is your code {{ discountCode }}",
                "user_id": user.pk,
                "utc-date": "2020-10-01T12:15:31-02:22",
                "status": "new",
            },
        ]

        for data in chats:
            timestamp = data.pop("utc-date")
            chat = Chat.objects.create(conversation=conversation, **data)
            Chat.objects.filter(pk=chat.pk).update(created_at=parse_datetime(timestamp))

        self.stdout.write(
            self.style.SUCCESS("Successfully created conversation")
        )
