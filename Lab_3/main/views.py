from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import date


def main(request):
    return render(request, 'main.html')


def health(request):
    response = {
        'date': date.today(),
        'current_page': request.build_absolute_uri(),
        'server_info': request.META['SERVER_NAME'],
        'client_info': {
            'user_agent': request.META['HTTP_USER_AGENT'],
            'user_ip': request.META['REMOTE_ADDR']
        }
    }
    return JsonResponse(response)

