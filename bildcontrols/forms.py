from django import forms

class BildCreationForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=300, required=True)
    tags = forms.CharField(max_length=100, required=True)