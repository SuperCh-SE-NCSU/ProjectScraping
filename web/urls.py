from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^subscribe/', include('subscribe.urls')),
   
)