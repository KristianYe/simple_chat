from rest_framework.permissions import IsAuthenticated


class CanAccessThread(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        if request.method in ("DELETE", "GET"):
            return request.user in obj.participants.all()

        return False
