from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("serach", views.SearchView.as_view(), name="search"),
    path(
        "login-musicbrainz",
        views.LoginMusicBrainzView.as_view(),
        name="login-musicbrainz",
    ),
    path("login-spotify", views.LoginSpotifyView.as_view(), name="login-spotify"),
]
