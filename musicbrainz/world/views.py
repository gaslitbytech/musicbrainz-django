from django.core.serializers import serialize
from django.http import JsonResponse
from django.views.generic.list import View, ListView

from .models import WorldBorder


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
