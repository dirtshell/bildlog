from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from bild.models import *
from bildloguser.models import *

def signup(request):
    if request.method == 'POST': # If the form has been submitted...
        if not request.POST['password1'] == request.POST['password2']:
            return HttpResponse("HOLY SHIT YOUR PASSWORDS DONT MATCH!")
        form = BildLogUserForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            password = request.POST['password1']
            username = request.POST['username']
            email = request.POST['email']
            BildLogUserManager.objects.create_user(
                email,
                username,
                password,
            )
            return HttpResponse('Huzzah! Success!')
    else:
        form = BildLogUserForm() # An unbound form
    return render(request, 'signup.html', {
        'form': form,
    })