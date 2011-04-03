from django.template import Context, loader
from django.http import HttpResponse

def index(request):    
    t = loader.get_template('index.html')
    c = Context({
        #'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(t.render(c))
