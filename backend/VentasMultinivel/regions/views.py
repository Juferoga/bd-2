import json
from django.shortcuts import render
import django.middleware.csrf
#import models
from .models import *
import datetime

# Create your views here.from django.http import HttpResponse


def get_regions(request):
    if request.method == 'GET':
        return render(request, 'Regions.json')


def get_countries(request):
    csrf = django.middleware.csrf.get_token(request)
    print(csrf)
    if request.method == 'GET':
        get_paises()
        return render(request, 'Countries.json')
    elif request.method == 'POST':
        start = datetime.datetime.now()
        data = json.loads(request.body)
        res = add_pais(data['nombre'])
        end = datetime.datetime.now()
        return render(request, 'Post.json', context={'status': 'Success', 'message': res, 'datos': [1, "b", False], 'status_code': 200, "response_time": (end - start).microseconds})
    elif request.method == 'PUT':
        return render(request, 'Put.json')
    elif request.method == 'DELETE':
        return render(request, 'Delete.json')

def get_csrf(request):
    csrf = django.middleware.csrf.get_token(request)
    print(csrf)
    return render(request, 'Csrf.html', context={'csrf': csrf})
