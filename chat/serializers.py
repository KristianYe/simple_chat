from rest_framework import serializers

from chat.models import Thread, Message
from user.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ("id", "sender", "text", "thread", "created", "is_read")


class ThreadSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Thread
        fields = ('id', 'participants', 'created', 'updated')


class ThreadListSerializer(ThreadSerializer):
    last_message = MessageSerializer(read_only=True)

    class Meta:
        model = Thread
        fields = ('id', 'participants', 'created', 'updated', 'last_message')
