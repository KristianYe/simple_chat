from rest_framework import serializers

from chat.models import Thread
from user.serializers import UserSerializer


class ThreadSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Thread
        fields = ['id', 'participants', 'created', 'updated']
