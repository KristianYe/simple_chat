from django.urls import path

from chat.views import ThreadViewSet

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


urlpatterns = [
    path("threads/", thread_list, name="thread-list"),
    path("threads/create/", thread_create, name="thread-create"),
    path("threads/<int:pk>/", thread_detail, name="thread-detail"),
]

app_name = "chat"
