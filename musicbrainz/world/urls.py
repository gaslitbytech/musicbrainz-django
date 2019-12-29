from django.urls import path

from . import views

app_name = "world"
urlpatterns = [
    path("border", views.WorldBorderListView.as_view(), name="border"),
]
