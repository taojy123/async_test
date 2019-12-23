from django.shortcuts import render, HttpResponse
import requests


def index(request):
    url = 'http://lovegaudi.art:3000'
    requests.get(url)
    return HttpResponse('hello')
    
    
