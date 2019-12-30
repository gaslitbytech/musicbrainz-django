"""
Utils needed on all projects
"""
import csv
import json
import logging
import types
import unicodedata
from collections import OrderedDict
from datetime import date, datetime
from decimal import Decimal
from inspect import isclass
from io import BytesIO, StringIO

import requests

import json_default
import jwt
from django.conf import settings
from django.conf.urls import url
from django.core.exceptions import ValidationError
from django.db import models, connection
from django.db.models import Case, CharField, Func, Q, Sum, Value, When
from django.db.models.functions import TruncMonth
from django.http import JsonResponse, StreamingHttpResponse


LOG = logging.getLogger(__file__)


# pylint: disable=invalid-name
class IsNull(Func):
    """ See supplier.models for usage """
    template = '%(expressions)s IS NULL'


@json_default.default.register(Decimal)
def _(o):  # pylint: disable=invalid-name
    '''Add support for Decimal to JSON'''
    return float(o)


class LocalJsonEncoder(json.JSONEncoder):
    '''
    Custom JSON encoder using json_default
    '''
    def default(self, o):  # pylint: disable=method-hidden
        '''Use json_default for unknown types.'''
        return json_default.default(o)


def json_response(queryset):
    return JsonResponse({'data': queryset}, encoder=LocalJsonEncoder)


def json_body(request):
    encoding = request.encoding or settings.DEFAULT_CHARSET
    return json.loads(request.body.decode(encoding))


decimal_field = models.DecimalField(0, 2)  # pylint: disable=invalid-name


def execute_raw_sql(query, columns=None, params=None):
    '''
    Execute provided raw sql query with extra filter params.
    Then calculate extra columns that api needs.
    '''
    with connection.cursor() as cur:
        cur.execute(query, params=params)
        data = cur.fetchall()

        if not columns:
            columns = [col[0] for col in cur.description]
        data = [dict(zip(columns, row)) for row in data]

    return data


class Patterns(list):
    '''
    Helper for generating urlpatterns lists.
    '''
    def __call__(self, pattern, kwargs=None, name=None):
        '''
        Act as a class or function decorator for appending a new url.
        '''
        def _inner(func):
            '''Actual decorator function'''
            if isclass(func):
                view = func.as_view()
            else:
                view = func
            self.append(url(pattern, view, kwargs=kwargs, name=name))
            return func
        return _inner


def map_report_format_to_extension(report_format):
    """
    Given report format name, return corresponding  extension.
    """
    maps = {
        REPORT_FORMAT.CSV: 'csv',
        REPORT_FORMAT.EXCEL: 'xlsx',
    }
    return maps[report_format]


def generate_rows(queryset):
    writer = Writer(queryset._fields)
    yield writer.write_headers()
    for row in queryset:
        yield writer.write_dict({
            k: str(v) if v is not None else ''
            for k, v in row.items()
        })


def csv_response(file_name, queryset):
    '''
    Stream a response with provided format to the browser.
    '''
    content_type = "text/csv; charset=utf-8"
    response = StreamingHttpResponse(generate_rows(queryset), content_type=content_type)
    response['Content-Disposition'] = 'attachment; filename=%s' % file_name
    return response


class DefaultValueDict(dict):
    ''' Custom class to handle recursive get.
    '''

    def __init__(self, *args, default=0, **kwargs):
        self.default = default
        super().__init__(*args, **kwargs)

    def iterget(self, *keys):
        ''' Attempts to return a value from a given dictionary based on a
            list of keys. If any of the keys returns a KeyError, returns
            `default` value.
        '''
        result = self
        for key in keys:
            try:
                result = result[key]
            except KeyError:
                return self.default
        return result
