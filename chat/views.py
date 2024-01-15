from rest_framework import generics
from rest_framework.views import APIView

from chat.models import Thread
from chat.serializers import ThreadListSerializer


class ThreadList(generics.ListAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadListSerializer

    def get_queryset(self):
        threads = self.queryset.filter(user=self.request.user)

        for thread in threads:
            last_message = thread.messages.last()
            thread.last_message = last_message

        return threads


