from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import render
from bildcontrols.models import *

def index(request):
    return render(request, 'index.html')

def createBild(request):
    return render(request, 'createbild.html')
    
def createLog(request):
    return render(request, 'createlog.html')

def submitBild(request):
    # Handle the form here
    return HttpResponse("You submitted a Bild")
    
def submitLog(request):
    # Handle the form here
    return HttpResponse("You submitted a log")