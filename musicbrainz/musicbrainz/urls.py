from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path("", include("entities.urls")),
    path("entities/", include("entities.urls")),  # kept for legacy
    path("admin/", admin.site.urls),
    url("", include("social_django.urls", namespace="social")),
]
