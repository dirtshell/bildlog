from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from bild.models import *
from bildloguser.models import *

def signup(request):
    if request.method == 'POST': # If the form has been submitted...
        if not request.POST['password1'] == request.POST['password2']:
                return render(request, 'signup.html', {
                    'error' : "Your passwords did not match. Please try again"
                })
        form = BildLogUserForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            password = request.POST['password1']
            username = request.POST['username']
            email = request.POST['email']
            User.objects.create_user(
                username,   # This order is important
                email,
                password,
            )
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            if user is not None: # login and send them to the index
                login(request, user) 
                return HttpResponseRedirect('/') 
            else:
                return render(request, 'signup.html', {
                    'error' : "A server error occured. Please try again"
                })
    else:
        form = BildLogUserForm() # An unbound form
    return render(request, 'signup.html', {
        'form': form,
    })