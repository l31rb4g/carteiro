import os
import json
import pytz
from django.http import JsonResponse
from app.settings import TIME_ZONE


MESES = [None, 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

def write_json(request, data=None, status=200):
    response = JsonResponse({} if data is None else data, status=status, safe=False)
    origin = os.environ.get('HTTP_ALLOW_ORIGIN', 'http://localhost:8000')
    response['Access-Control-Allow-Origin'] = origin
    response['Content-type'] = 'application/json; charset=utf-8'
    response['Access-Control-Allow-Credentials'] = 'true'
    response['Access-Control-Allow-Headers'] = 'content-type, x-request, x-requested-with'
    return response


def read_json(request):
    if request and request.body:
        data = json.loads(request.body)
        return data
    return {}


def localdate(date=None):
    if not date:
        date = datetime.datetime.now()
    return date.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(TIME_ZONE))
