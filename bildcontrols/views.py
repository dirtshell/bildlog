from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import render
from bildloguser.models import *
from bildcontrols.models import *
from django.contrib.auth.models import User
from django.db.models import Count
from forms import *

def index(request):
    return render(request, 'index.html')

def createBild(request):
    if request.method == 'POST': # If the form has been submitted...
        form = BildCreationForm(request.POST) # A form bound to the POST data
        if request.user.is_authenticated(): # A little bit of extra safety
            if form.is_valid(): # All validation rules pass
                # Process the data in form.cleaned_data
                owner = User.objects.get(username=request.user)
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                tag_string = form.cleaned_data['tags'] # The tags in CSV form
                
                # Construct the Bild object
                bild = Bild.objects.create(title=title, description=description, owner=owner) # Create the bild object
                tags = tag_string.split(',') # Process the tag_string CSV and convert it to a list
                for tag in tags:
                    bild.tags.add(tag.strip()) # Cycle through the tags, strip them, and add them to the bild
                bild.save() # Finally, save the completed Bild
                
                return HttpResponse("HUZZAH YOU CREATED A BILD") # The success page
    else:
        form = BildCreationForm() # An unbound (empty) form

    return render(request, 'createbild.html', {
        'form': form,
    })
    
def createLog(request):
    return render(request, 'createlog.html')
    
def user_profile(request, username):
    try:
        u = User.objects.get(username=username)
        user = u.get_profile()
        username = u.username
        #print username
        rep = user.rep
        #print "Rep: %s" % rep
        followers_total = user.followers.count()
        #print "Follower: %s" % followers_total
        following_total = user.following.count()
        #print "Following: %s" % following_total
        return render(request, 'profile.html', {
            'username':username,
            'rep':rep,
            'follower_total':followers_total,
            'following_total':following_total,
        })
    except:
        return render(request, 'error.html', {
                'error':"It would seem that the user you are looking for does not exist",
        })