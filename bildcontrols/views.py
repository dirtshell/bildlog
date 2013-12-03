from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import render
from bildloguser.models import *
from bildcontrols.models import *
from django.contrib.auth.models import User
from django.db.models import Count

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
    if request.method == 'POST': # If the form has been submitted...
        form = LogCreationForm(user=request.user, data=request.POST) # A form bound to the POST data
        if request.user.is_authenticated(): # A little bit of extra safety
            if form.is_valid(): # All validation rules pass
                # Process the data in form.cleaned_data
                owner = request.user
                title = form.cleaned_data['title']
                body = form.cleaned_data['body']
                tag_string = form.cleaned_data['tags'] # The tags in CSV form
                bilds = Bild.objects.filter(owner=User.objects.get(username=owner))    # The Bild the log is tied to
                bild = bilds[int(form.cleaned_data['bild'])] # Convert the unicode key to an int and assign it as the Bild
                
                # Construct the Log object
                log = Log.objects.create(owner=owner, title=title, body=body, bild=bild) # Create the log object
                tags = tag_string.split(',') # Process the tag_string CSV and convert it to a list
                for tag in tags:
                    log.tags.add(tag.strip()) # Cycle through the tags, strip them, and add them to the bild
                log.save() # Finally, save the completed Bild
                
                return HttpResponse("HUZZAH YOU CREATED A LOG") # The success page
    else:
        form = LogCreationForm(user=request.user) # An unbound (empty) form

    return render(request, 'createlog.html', {
        'form': form,
    })
    
def user_profile(request, username, active=""):
    #try: # Uncoment this when on deploy
        
    u = User.objects.get(username=username)
    user = u.get_profile()
    
    if user is not None: #  Comment on deploy
        # Basic user info for displaying in the left hand pane
        language_list = [] # Initialize the array so I can add to it
        username = u.username
        rep = user.rep
        job = user.job
        country = user.country
        github = user.github
        bitbucket = user.bitbucket
        personal_site = user.personal_site
        contact = user.contact
        join_date = user.user.date_joined.date
        followers_total = user.followers.count()
        following_total = user.following.count()
        languages = user.languages.all()	# Gather all language objects
        for language in languages:	# Cycle through and add them to the language list
        		language_list.append(language.language)
        language_string = ", ".join(language_list) # Convert the language list to a comma seperated string
		
		# Assembling the Bild list
        bilds_list = Bild.objects.filter(owner=user) # Collect a list of the bilds by the user
        
        # Assembling the Log list
        logs_list = Log.objects.filter(owner=user) # Collect a list of the logs by the user
        
        # Determining the panel to show on load
        while active not in ({"bilds", "activity", "logs", "code"}):
            active = "bilds" # If not one of the options, show the default Bilds panel
		
        return render(request, 'profile.html', {
            'username':username,
            'rep':rep,
			'country':country,
            'followers_total':followers_total,
            'following_total':following_total,
			'languages':language_string,
			'personal_site':personal_site,
			'join_date':join_date,
			'github':github,
			'bitbucket':bitbucket,
			'contact':contact,
			'job':job,
			'bilds':bilds_list,
			'logs':logs_list,
			'active_panel':active,  # The panel that the page shows on load, defaults to Bilds
        })
    #except:    # Uncomment this when on deploy
    else:   # Comment this on deploy
        return render(request, 'error.html', {
                'error':"It would seem that the user you are looking for does not exist",
        })
        
def bild(request, username, bild_name):
    return render(request, 'bild.html')