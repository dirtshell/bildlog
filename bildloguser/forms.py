from django import forms
from bildloguser.models import BildLogUser

class SignUpForm(forms.ModelForm):
    #email                       =           forms.EmailField(max_length=150, required=True)
    #username                    =           forms.CharField(max_length=30, required=True)
    #password1                   =           forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=30, required=True)
    #password2                   =           forms.CharField(label='Password confirmation', widget=forms.PasswordInput(), max_length=30, required=True)
    
    class Meta:
        model = BildLogUser
        fields = ['email', 'username', 'password']