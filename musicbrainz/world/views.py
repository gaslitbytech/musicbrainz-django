from django.core.serializers import serialize
from django.http import JsonResponse
from django.views.generic.list import View, ListView

from .models import WorldBorder, Location


# see class based views
class WorldBorderListView(ListView):
    model = WorldBorder

    def get(self, *args, **kwargs):
        return JsonResponse({
            'data': serialize(
                'geojson', WorldBorder.objects.all(),
                geometry_field='mpoly',
                fields=('name', 'pop2005',)
            )
        })


class LocationListView(ListView):
    model = Location

    def get(self, *args, **kwargs):
        return JsonResponse({
            'data': serialize(
                'geojson', Location.objects.all(),
                geometry_field='position',
                fields=('iata', 'name',)
            )
        })
