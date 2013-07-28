from django.db import models
from django import forms
from django.conf import settings
from taggit.managers import TaggableManager
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class BildLogUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            username=username,    
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class BildLogUser(AbstractBaseUser):
    # Last login, is active, and password are included automatically
    username                        =       models.CharField(max_length=30, blank=False, unique=True, )
    email                           =       models.EmailField(max_length=150, blank=False)
    join_date                       =       models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = BildLogUserManager()
    
class BildLogUserForm(forms.Form):
    email                       =           forms.EmailField(max_length=150, required=True)
    username                    =           forms.CharField(max_length=30, required=True)
    password1                   =           forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=30, required=True)
    password2                   =           forms.CharField(label='Password confirmation', widget=forms.PasswordInput(), max_length=30, required=True)