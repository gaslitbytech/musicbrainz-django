import logging

from django.db.models import Q
from django.contrib.gis.geos import Polygon, GEOSGeometry
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import View, ListView

from .models import WorldBorder, Location


LOG = logging.getLogger(__name__)


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
        """
        Use current map bounds to get the locations within the users map view.
        """
        # TODO remove random coords
        xmin=self.request.GET.get('west') or '0'
        ymin=self.request.GET.get('south') or '0'
        xmax=self.request.GET.get('east') or '0'
        ymax=self.request.GET.get('north') or '0'
        bbox = (xmin, ymin, xmax, ymax)
        geom = Polygon.from_bbox(bbox)

        # TODO Went back to Postgresql 11 and postgis 2.5 for this query.
        # https://trac.osgeo.org/postgis/ticket/4608

        return HttpResponse(
            serialize(
                'geojson', Location.objects.filter(
                    position__coveredby=geom
                ).all(),
                geometry_field='position',
                fields=('iata', 'name',)
            )
        )
