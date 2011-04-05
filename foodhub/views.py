from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response


def index(request):    
    t = loader.get_template('index.html')
    c = Context({
        #'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(t.render(c))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/recipehub/")
    else:
        form = UserCreationForm()
    return render_to_response("register.html", {
        'form': form,
    }, context_instance=RequestContext(request))
