from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import reverse, redirect
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from chat.models import Thread
from chat.serializers import ThreadSerializer, ThreadListSerializer


class ThreadViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

    def get_queryset(self):
        queryset = self.queryset

        if self.action == "list":
            queryset = queryset.filter(participants=self.request.user)
            for thread in queryset:
                last_message = thread.messages.last()
                thread.last_message = last_message

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return ThreadListSerializer

        return self.serializer_class

    def create(self, request, *args, **kwargs):
        participants = request.data.get("participants")

        try:
            thread = Thread.objects.get(participants=participants)
        except ObjectDoesNotExist:
            return super().create(request, *args, **kwargs)

        thread_detail_url = reverse("chat:thread-detail", kwargs={"pk": thread.pk})

        return redirect(thread_detail_url)
