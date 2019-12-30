from django.urls import path

from . import views

app_name = "world"
urlpatterns = [
    path("border", views.WorldBorderListView.as_view(), name="border"),
    path("location", views.LocationListView.as_view(), name="location"),
]
