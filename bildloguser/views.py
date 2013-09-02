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

# Edit your profile
def edit_profile(request):
    if not request.user.is_authenticated():
        return render(request, 'error.html', {
            'error':"Welp, looks like you gunna have to login to do that."
        })
    else:
        u = request.user
        user = u.get_profile()
        if request.method == 'POST':
            user.personal_site = request.POST['personal_site'].strip()
            user.job = request.POST['job']
            user.country = request.POST['country']
            user.github = request.POST['github']
            user.bitbucket = request.POST['bitbucket']
            user.contact = request.POST['contact']
            
            languages = request.POST['languages'].split(',')  # Split up the languages and add them
            for language in languages:
                if Language.objects.get(language=language) is None: # If the language does not already exist in the database, add it to the database and to the users languages
                    new_language = Language.objects.create(language=language.strip())
                    new_language.save()
                    user.languages.add(new_language)
                else:   # If the language is already in the database
                    user.languages.add(Languages.objects.get(language=language.strip()))
                
            user.save() # Save the user
            return render(request, 'profile.html') # Need to add the context
        else:
            # Need to populate this with values
            form = BildLogUserProfileForm()
            return render(request, 'profileedit.html', {
                'form': form,
            })

# View a user's account
# If the user viewing the page is the user of the page, then link to bildcontrols and user settings
def user_profile(request):
    return render(request, 'userprofile.html')
