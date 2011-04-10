from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^register', 'foodhub.views.register', name='register'),
    url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout', 'foodhub.views.logout_view'),
    url(r'^create', 'foodhub.views.create'),
    url(r'^$', 'foodhub.views.index', name='index'),    
    # url(r'^recipehub/', include('recipehub.foo.urls')),
)
