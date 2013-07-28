from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from bild.models import *

def index(request):
    return render(request, 'index.html')
