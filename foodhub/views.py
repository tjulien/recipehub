from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from foodhub.forms import AccountCreationForm

def index(request):
    return render_to_response('index.html', RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password2'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/recipehub/')                
    else:
        form = AccountCreationForm()
    return render_to_response('register.html', {
                'form': form,
                }, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/recipehub')

def create(request):
    return render_to_response('recipe.html', RequestContext(request))
