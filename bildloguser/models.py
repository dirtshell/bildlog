from django.db import models
from django import forms
from django.conf import settings
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class BildLogUser(models.Model):
    user                        =           models.OneToOneField(User)          # The django auth user this profile is tied to
    verified                    =           models.BooleanField(default=0)      # Users must click an email link to verify and post comments
    personal_site               =           models.CharField(max_length=100)    # Dont know if I want to include this
    
class BildLogUserForm(forms.Form):
    username                    =           forms.CharField(max_length=30, required=True)
    email                       =           forms.EmailField(max_length=150, required=True)
    password1                   =           forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=30, required=True)
    password2                   =           forms.CharField(label='Password confirmation', widget=forms.PasswordInput(), max_length=30, required=True)