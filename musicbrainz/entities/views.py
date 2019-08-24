import logging

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import View, ListView 
import requests

from .forms import ArtistSearchForm

LOG = logging.getLogger(__name__)


class LoginMusicBrainzView(View):
    template_name = "entities/login_musicbrainz.html"

    def get_queryset(self, **kwargs):
        return []


class LoginSpotifyView(ListView):
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
            LOG.debug('form is valid: data: %s', form.cleaned_data)
            
            user = request.user
            social = user.social_auth.get(provider="musicbrainz")

            # remove nulls from search list
            data = {k:v for k, v in form.cleaned_data.items() if v}
            data.update(
                {
                    "fmt":"json",
                    "query": "artist",
                    "access_token": social.extra_data["access_token"],
                }
            )

            url = "https://musicbrainz.org/ws/2/artist"
            LOG.debug("URL: %s", url)
            r = requests.get(
                url,
                params=data
            )
            if r.status_code == requests.codes.ok:
                data = r.json()
                LOG.debug(data)

            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})


class IndexView(ListView):
    template_name = "entities/index.html"

    def get_queryset(self, **kwargs):
        return []
