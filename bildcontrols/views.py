from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import render
from bildcontrols.models import *

def index(request):
    return render(request, 'index.html')

def createBild(request):
    return HttpResponse("You submitted a Bild")
    
def createLog(request):
    return HttpResponse("You submitted a log")