from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
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


class ThreadCreateSerializer(serializers.Serializer):
    participant_id = serializers.IntegerField()

    def validate_participant_id(self, value):
        try:
            get_user_model().objects.get(id=value)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(f"There is no user with id {value}")

        return value

    def save(self):
        user_id = self.context["request"].user.id
        participant_id = self.validated_data["participant_id"]

        thread = Thread.objects.create()
        thread.participants.set([user_id, participant_id])

        return thread
