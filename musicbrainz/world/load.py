import csv
import os

from django.contrib.gis.geos import Point
from django.contrib.gis.utils import LayerMapping
from django.core.exceptions import ObjectDoesNotExist

from .models import WorldBorder, Location


"""
The following is based on geodjango
"""
world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'TM_WORLD_BORDERS-0.3.shp'),
)

def run_world(verbose=True):  # this was called run
    lm = LayerMapping(WorldBorder, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


"""
The following is to import data sourced from https://openflights.org/data.html
"""
airports_dat_file = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'airports-extended.dat'),
)


def run_airports():
    reader = csv.DictReader(
        open(airports_dat_file), 
        fieldnames=[
            "Airport ID",  #  Unique OpenFlights identifier for this airport.
            "Name",  #	Name of airport. May or may not contain the City name.
            "City",  #	Main city served by airport. May be spelled differently from Name.
            "Country",  #	Country or territory where airport is located. See countries.dat to cross-reference to ISO 3166-1 codes.
            "IATA",  #	3-letter IATA code. Null if not assigned/unknown.
            "ICAO",  #	4-letter ICAO code.
            # "Null",  # if not assigned.
            "Latitude",  #	Decimal degrees, usually to six significant digits. Negative is South, positive is North.
            "Longitude",  #	Decimal degrees, usually to six significant digits. Negative is West, positive is East.
            "Altitude",  #	In feet.
            "Timezone",  #	Hours offset from UTC. Fractional hours are expressed as decimals, eg. India is 5.5.
            "DST",  #	Daylight savings time. One of E (Europe), A (US/Canada), S (South America), O (Australia), Z (New Zealand), N (None) or U (Unknown). See also: Help: Time
            "Tz",  # database time zone	Timezone in "tz" (Olson) format, eg. "America/Los_Angeles".
            "Type",  #	Type of the airport. Value "airport" for air terminals, "station" for train stations, "port" for ferry terminals and "unknown" if not known. In airports.csv, only type=airport is included.
            "Source",  #	Source of this data. "OurAirports" for data sourced from OurAirports, "Legacy" for old data not matched to OurAirports (mostly DAFIF), "User" for unverified user contributions. In airports.csv, only source=OurAirports is included.
        ]
    )
    for row in list(reader):
        try:
            location = Location.objects.get(airport_id=row['Airport ID'])
        except ObjectDoesNotExist:
            print(row)
            location = Location(airport_id=row['Airport ID'])
            location.name = row["Name"]
            location.city = row["City"]
            location.country = row["Country"]
            location.iata = row["IATA"]
            location.icao = row["ICAO"]
            # location.null = row["Null"]
            location.latitude = float(row["Latitude"])
            location.longitude = float(row["Longitude"])
            location.altitude = row["Altitude"]
            location._timezone = float(row["Timezone"] if row["Timezone"] != "\\N" else 0.0)
            location._dst = row["DST"] if row["DST"] != "\\N" else None
            location.tz = row["Tz"] if row["Tz"] != "\\N" else None
            location.type = row["Type"]
            location.source = row["Source"]
            location.position=Point(location.longitude, location.latitude, srid=4326)
            location.save()
