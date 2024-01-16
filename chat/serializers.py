from rest_framework import serializers

from chat.models import Thread, Message
from user.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ("id", "sender", "text", "thread", "created", "is_read")


class MessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ("text", )


class ReadMessagesSerializer(serializers.Serializer):
    message_ids = serializers.ListField(child=serializers.IntegerField())

    def validate_message_ids(self, value):
        if not Message.objects.filter(id__in=value).exists():
            raise serializers.ValidationError(
                "One or more message IDs do not exist in the database."
            )

        return value


class ThreadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thread
        fields = ("id", "participants", "created", "updated")


class ThreadListSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    last_message = MessageSerializer(read_only=True)

    class Meta:
        model = Thread
        fields = ("id", "participants", "created", "updated", "last_message")
