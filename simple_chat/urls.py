from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("api/chat/", include("chat.urls", namespace="chat")),
    path("api/user/", include("user.urls", namespace="user")),
]
