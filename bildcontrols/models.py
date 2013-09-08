from django.db import models
from django.conf import settings
from bildloguser.models import *
from django import forms
from taggit.managers import TaggableManager

# Create your models here.
class Bild(models.Model):
    bild_id                         =       models.AutoField(primary_key=True)
    owner                           =       models.ForeignKey(settings.AUTH_USER_MODEL)
    title                           =       models.CharField(max_length=100)
    creation_date                   =       models.DateTimeField(auto_now_add = True)
    last_updated                    =       models.DateTimeField(auto_now = True)
    description                     =       models.CharField(max_length=300)
    activated                       =       models.BooleanField(default=True)
    tags                            =       TaggableManager()

class Log(models.Model):
    log_id                          =       models.AutoField(primary_key=True)
    bild                            =       models.ForeignKey(Bild)
    creation_date                   =       models.DateTimeField(auto_now_add = True)
    last_updated                    =       models.DateTimeField(auto_now = True)
    title                           =       models.CharField(max_length=100)
    body                            =       models.TextField()
    activated                       =       models.BooleanField(default=True)
    tags                            =       TaggableManager()

class BildCreationForm(forms.Form):
    title                           =       forms.CharField(label="Title", max_length=100, required=True)
    description                     =       forms.CharField(label="Description", max_length=300, required=True)
    tags                            =       forms.CharField(label="Tags", max_length=100, required=True)