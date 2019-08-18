from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login-musicbrainz', views.LoginMusicBrainzView.as_view(), name='login-musicbrainz'),
    path('login-spotify', views.LoginSpotifyView.as_view(), name='login-spotify'),    
]
