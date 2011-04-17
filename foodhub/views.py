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
    recipe.save()
    return render_to_response('recipe.html', {'recipe': recipe,
                                              'recipe_name': 'Recipe name - click to edit', #recipe.name,
                                              'ingredients': recipe.ingredient_set.values(),
                                              'token': request.META['CSRF_COOKIE']}, RequestContext(request))
@login_required
def recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk = recipe_id)
    if request.method == 'POST':
        setattr(recipe, request.POST['id'], request.POST['value']) 
        recipe.save()
    if len(recipe.name.strip()) == 0:
        recipe.name = 'Recipe name - click to edit'
    return render_to_response('recipe.html', {'recipe': recipe,
                                              'recipe_name': recipe.name,
                                              'ingredients': recipe.ingredient_set.values(),
                                              'token': request.META['CSRF_COOKIE']}, RequestContext(request))
@login_required
def ingredient(request, recipe_id):
    if request.method == 'POST':
        recipe = Recipe.objects.get(pk = recipe_id)
        ingredient_id = request.POST['id']
        if ingredient_id is not None:
            ingredient_id = ingredient_id.strip()
        if ingredient_id is not None and len(ingredient_id) > 0:
            ingredient = Ingredient.objects.get(pk = ingredient_id)
        else:
            ingredient = Ingredient.objects.create(list_num = len(recipe.ingredient_set.values()),
                                                   recipe = recipe)
        ingredient.name = request.POST['value']
        ingredient.save()
        return HttpResponse(request.POST['value'])


    #if request.method == 'POST':
    #    setattr(recipe, fieldname, fieldvalue) 
    #    my_instance.save() 
