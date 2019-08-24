import logging

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import View

from .forms import ArtistSearchForm

LOG = logging.getLogger(__name__)


class LoginMusicBrainzView(View):
    template_name = "entities/login_musicbrainz.html"

    def get_queryset(self, **kwargs):
        return []


class LoginSpotifyView(View):
    template_name = "entities/login_spotify.html"

    def get_queryset(self, **kwargs):
        return []


# Learning from https://docs.djangoproject.com/en/2.2/topics/class-based-views/intro/#handling-forms-with-class-based-views
class SearchView(View):
    form_class = ArtistSearchForm
    initial = {'': ''}
    template_name = "entities/search_template.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})


class IndexView(View):
    template_name = "entities/index.html"

    def get(self, **kwargs):
        return []
