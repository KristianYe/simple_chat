from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated, BasePermission

from chat.models import Thread


class CanAccessThread(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        if request.method in ("DELETE", "GET"):
            return request.user in obj.participants.all()

        return False


class CanAccessMessages(BasePermission):
    def has_permission(self, request, view):
        thread_id = view.kwargs["pk"]
        try:
            thread = Thread.objects.get(id=thread_id)
        except ObjectDoesNotExist:
            return False
        return bool(thread and request.user in thread.participants.all())


