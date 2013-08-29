from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from bildcontrols.models import *
from bildloguser.models import *

# Register a user and login them in
# This could probably use better error handling and display
def signup(request):
    if request.method == 'POST': # If the form has been submitted...
        form = BildLogUserForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            password = request.POST['password1']
            username = request.POST['username']
            email = request.POST['email1']
            User.objects.create_user(
                username,   # This order is important
                email,
                password,
            )
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            bu = BildLogUser(user=user)
            bu.save()
            if user is not None: # login and send them to the index
                login(request, user) 
                return HttpResponseRedirect('/') 
            else:
                return render(request, 'signup.html', {
                    'server_error' : "A server error occured. Please try again",
                })
    else:
        form = BildLogUserForm() # An unbound form
    return render(request, 'signup.html', {
        'form': form,
    })

# Log out a user
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
    
# Log in a user
# This could probably use better error handling and display
def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['user_username'], password=request.POST['user_password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'index.html', {
                'login_error' : "Login failed",
            })  
    else:
        return render(request, 'index.html', {
            'login_error' : "Login failed",
        })
    
# View a user's account
# If the user viewing the page is the user of the page, then link to bildcontrols and user settings
def user_profile(request):
    return render(request, 'userprofile.html')
