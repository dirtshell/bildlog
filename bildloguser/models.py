from django.db import models
from django import forms
from django.conf import settings
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Language(models.Model):
    language                    =           models.CharField(max_length=20, null=False, unique=True) 
    creation_date               =           models.DateTimeField(auto_now_add = True)
    
    def language_list(self):
        return ', '.join([l.language for l in self.language.all()])
    language_list.short_description = "Languages in a list"

class BildLogUser(models.Model):
    user                        =           models.OneToOneField(User)          # The django auth user this profile is tied to
    verified                    =           models.BooleanField(default=0)      # Users must click an email link to verify and post comments
    personal_site               =           models.CharField(max_length=100, null=True)    # Dont know if I want to include this
    languages                   =           models.ManyToManyField(Language, null=True)    # The languages the user knows             
    job                         =           models.CharField(max_length=50, null=True)     # The users occupation
    country                     =           models.CharField(max_length=50, null=True)     # The users country
    github                      =           models.CharField(max_length=50, null=True)     # The users github account
    bitbucket                   =           models.CharField(max_length=50, null=True)     # The users bitbucket account
    contact                     =           models.EmailField(null=True)        # The email the user would like people to contact him with
    rep                         =           models.BigIntegerField(default=0, null=True)            # The users rep
    followers                   =           models.ManyToManyField('self', related_name='follower', symmetrical=False, null=True)  # Followers of the user
    following                   =           models.ManyToManyField('self', related_name='followed', symmetrical=False, null=True)  # Users the user is following
    
class BildLogUserForm(forms.Form):
    username                    =           forms.CharField(label='username', max_length=30, required=True)
    email1                      =           forms.EmailField(label='Email', max_length=150, required=True)
    email2                      =           forms.EmailField(label='Email confirmation', max_length=150, required=True)
    password1                   =           forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=30, required=True)
    password2                   =           forms.CharField(label='Password confirmation', widget=forms.PasswordInput(), max_length=30, required=True)
    
class BildLogUserProfileForm(forms.Form):
    personal_site               =           forms.CharField(label='Personal Site', required=False,max_length=100)
    languages                   =           forms.CharField(label='Languages (Comma seperated)', required=False, max_length=200)         
    job                         =           forms.CharField(label='Job', required=False, max_length=50)
    country                     =           forms.CharField(label='Country', required=False, max_length=50)
    github                      =           forms.CharField(label='Github', required=False, max_length=50) # May hav eimproper caps here
    bitbucket                   =           forms.CharField(label='BitBucket', required=False, max_length=50)
    contact                     =           forms.CharField(label='Contact Email', required=False, max_length=100)