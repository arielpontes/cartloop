from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Store(models.Model):
    timezone = models.CharField(max_length=100, default=settings.TIME_ZONE)


class OperatorGroup(models.Model):
    name = models.CharField(max_length=100)


class Operator(models.Model):
    group = models.ForeignKey(
        OperatorGroup, on_delete=models.SET_NULL, null=True
    )


class Conversation(models.Model):
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    operator = models.ForeignKey(
        Operator, on_delete=models.SET_NULL, null=True
    )
    client_id = models.PositiveSmallIntegerField(null=True)
    discount_code = models.CharField(max_length=20, blank=True)


class Chat(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="chats")
    payload = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    NEW = "new"
    SENT = "SENT"
    STATUS_CHOICES = [
        (NEW, "New"),
        (SENT, "Sent"),
    ]

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=NEW
    )


# class Schedule(models.Model):
#     chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
