from django.conf.urls import patterns, include, url
from django.contrib import admin
from soahw.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'soahw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',home),
    url(r'^hello/',hello),
    url(r'^users/',users),
    url(r'^posts/',posts),
    url(r'^access/',access),
)
