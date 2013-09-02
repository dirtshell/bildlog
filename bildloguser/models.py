from django.db import models
from django import forms
from django.conf import settings
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Language(models.Model):
    language                    =           models.CharField(max_length=20, null=False, unique=True) 
    creation_date               =           models.DateTimeField(auto_now_add = True)
    last_updated                =           models.DateTimeField(auto_now = True)

class BildLogUser(models.Model):
    user                        =           models.OneToOneField(User)          # The django auth user this profile is tied to
    verified                    =           models.BooleanField(default=0)      # Users must click an email link to verify and post comments
    personal_site               =           models.CharField(max_length=100)    # Dont know if I want to include this
    languages                   =           models.ManyToManyField(Language)    # The languages the user knows             
    job                         =           models.CharField(max_length=50)     # The users occupation
    country                     =           models.CharField(max_length=50)     # The users country
    github                      =           models.CharField(max_length=50)     # The users github account
    bitbucket                   =           models.CharField(max_length=50)     # The users bitbucket account
    contact                     =           models.EmailField()                 # The email the user would like people to contact him with
    rep                         =           models.BigIntegerField()            # The users rep
    followers                   =           models.ManyToManyField('self', related_name='follower', symmetrical=False)  # Followers of the user
    following                   =           models.ManyToManyField('self', related_name='followed', symmetrical=False)  # Users the user is following
    
class BildLogUserForm(forms.Form):
    username                    =           forms.CharField(max_length=30, required=True)
    email1                      =           forms.EmailField(max_length=150, required=True)
    email2                      =           forms.EmailField(max_length=150, required=True)
    password1                   =           forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=30, required=True)
    password2                   =           forms.CharField(label='Password confirmation', widget=forms.PasswordInput(), max_length=30, required=True)