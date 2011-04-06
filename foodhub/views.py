from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from foodhub.forms import AccountCreationForm

def index(request):    
    #t = loader.get_template('index.html')
    #c = Context({
        #'latest_poll_list': latest_poll_list,
    #})
    return render_to_response("index.html", RequestContext(request))#HttpResponse(t.render(c))

def register(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password2'])
            if user is not None:
                login(request, user)
                #return HttpResponseRedirect("/recipehub/")
                return render_to_response("index.html", {}, context_instance=RequestContext(request))
    else:
        form = AccountCreationForm()
    return render_to_response("register.html", {
                'form': form,
                }, context_instance=RequestContext(request))
