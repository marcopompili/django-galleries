'''
Created on 19/mag/2013

@author: Marco Pompili
'''

from django.conf.urls import patterns, url
from django.views.generic import ListView
from .models import Gallery

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
        queryset=Gallery.objects.all()[:],
        context_object_name='galleries',
        template_name='galleries/index.html'
    ), name = 'index'),
    url('^(?P<pk>\d+)/$', 'galleries.views.gallery'),
)