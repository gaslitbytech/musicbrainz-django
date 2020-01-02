from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import pytz


TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

"""
sourced from https://openflights.org/data.html
"""
class Location(models.Model):
    airport_id = models.IntegerField('Airport ID')  #  	Unique OpenFlights identifier for this airport.
    name = models.TextField('Name', null=True, blank=True)  # 	Name of airport. May or may not contain the City name.
    city = models.TextField('City', null=True, blank=True)  # 	Main city served by airport. May be spelled differently from Name.
    country = models.TextField('Country', null=True, blank=True)  # 	Country or territory where airport is located. See countries.dat to cross-reference to ISO 3166-1 codes.
    iata = models.CharField('IATA', max_length=3, null=True, blank=True)  # 	3-letter IATA code. Null if not assigned/unknown.
    icao = models.CharField('ICAO', max_length=4, null=True, blank=True)  # 	4-letter ICAO code.
    is_active = models.TextField('Null', null=True, blank=True)  #  if not assigned.
    latitude = models.FloatField('Latitude')  # 	Decimal degrees, usually to six significant digits. Negative is South, positive is North.
    longitude = models.FloatField('Longitude')  # 	Decimal degrees, usually to six significant digits. Negative is West, positive is East.
    altitude = models.IntegerField('Altitude')  # 	In feet.
    _timezone = models.FloatField('Timezone', null=True)  # 	Hours offset from UTC. Fractional hours are expressed as decimals, eg. India is 5.5.
    _dst = models.CharField('DST', max_length=1, null=True, blank=True)  # 	Daylight savings time. One of E (Europe), A (US/Canada), S (South America), O (Australia), Z (New Zealand), N (None) or U (Unknown). See also: Help: Time
    tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC', null=True, blank=True)  #  database time zone	Timezone in "tz" (Olson) format, eg. "America/Los_Angeles".
    location_type = models.TextField('Type', null=True, blank=True)  # 	Type of the airport. Value "airport" for air terminals, "station" for train stations, "port" for ferry terminals and "unknown" if not known. In airports.csv, only type=airport is included.
    source = models.TextField('Source', null=True, blank=True)  # 	Source of this data. "OurAirports" for data sourced from OurAirports, "Legacy" for old data not matched to OurAirports (mostly DAFIF), "User" for unverified user contributions. In airports.csv, only source=OurAirports is included.

    position = models.PointField(default=Point(0, 0), blank=True, geography=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.iata


class MapBoundView(models.Model):
    north = models.FloatField('North', blank=True, null=True)
    south = models.FloatField('South', blank=True, null=True)
    east = models.FloatField('East', blank=True, null=True)
    west = models.FloatField('West', blank=True, null=True)
    zoom = models.IntegerField('Zoom', blank=True, null=True)
