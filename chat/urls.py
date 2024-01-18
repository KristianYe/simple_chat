from django.urls import path

from chat.views import ThreadViewSet, MessageViewSet, UnreadMessagesCountView

thread_list = ThreadViewSet.as_view(actions={
    "get": "list",
})

thread_create = ThreadViewSet.as_view(actions={
    "post": "create",
})

thread_detail = ThreadViewSet.as_view(actions={
    "get": "retrieve",
    "delete": "destroy",
})

messages = MessageViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})

read_messages = MessageViewSet.as_view(actions={
    "post": "read_messages",
})

urlpatterns = [
    path("threads/", thread_list, name="thread-list"),
    path("threads/create/", thread_create, name="thread-create"),
    path("threads/<int:pk>/", thread_detail, name="thread-detail"),
    path("threads/<int:pk>/messages/", messages, name="messages"),
    path("threads/<int:pk>/messages/read/", read_messages, name="read-messages"),
    path('unread-messages-count/', UnreadMessagesCountView.as_view(), name="unread-messages-count")
]

app_name = "chat"
