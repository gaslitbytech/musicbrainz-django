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
        # (Q(country="Australia") | Q(country="Mexico"))
        # North:23.003908026630658
        # South:18.380592091462194
        # East:-86.62170410156251
        # West:-91.56555175781251

        north = self.request.GET.get('north') or '23.003908026630658'
        south = self.request.GET.get('south') or '18.380592091462194'
        east = self.request.GET.get('east') or '-86.62170410156251'
        west = self.request.GET.get('west') or '-91.56555175781251'

        ne = (north, east)
        sw = (south, west)
        xmin=sw[1]
        ymin=sw[0]
        xmax=ne[1]
        ymax=ne[0]
        bbox = (xmin, ymin, xmax, ymax)

        geom = Polygon.from_bbox(bbox)

        # TODO
        # Went back to Postgresql 11 and postgis 2.5 for this.
        # https://trac.osgeo.org/postgis/ticket/4608

        print(f'bbox:{bbox}')
        return HttpResponse(
            serialize(
                'geojson', Location.objects.filter(
                    position__coveredby=geom
                ).all(),
                geometry_field='position',
                fields=('iata', 'name',)
            )
        )
