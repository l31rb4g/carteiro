import re
from django.shortcuts import redirect, HttpResponse


def auth(get_response):

    def auth(request):
        OPEN_URLS = ['/login', '/hook']
        allow = False

        if request.path in OPEN_URLS:
            allow = True
        
        elif 'user' in request.session:
            allow = True

        return get_response(request) if allow else redirect('/login')

    return auth


