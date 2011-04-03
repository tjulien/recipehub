from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'foodhub.views.index', name='index'),
    # url(r'^recipehub/', include('recipehub.foo.urls')),
)
