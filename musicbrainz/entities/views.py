from django.http import HttpResponse
from django.views.generic.list import ListView


class LoginView(ListView):
    template_name = 'entities/login.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self, **kwargs):
        return []


class LoginSpotifyView(ListView):
    template_name = 'entities/login_spotify.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self, **kwargs):
        return []


class IndexView(ListView):
    template_name = 'entities/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self, **kwargs):
        return []
