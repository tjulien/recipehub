from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from foodhub.forms import AccountCreationForm
from foodhub.models import *
from datetime import *

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

@login_required
def create(request):
    recipe = Recipe.objects.create(user = request.user, create_date = datetime.now())
    return render_to_response('recipe.html', {'recipe': recipe, 
                                              'ingredients': recipe.ingredient_set.values()}, RequestContext(request))
