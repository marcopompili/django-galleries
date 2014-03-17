"""
Created on 19/mag/2013

@author: Marco Pompili
"""

from django.conf.urls import patterns, url
from django.views.generic import ListView
from .models import Gallery

urlpatterns = patterns('',
                       url(r'^$', ListView.as_view(
                           queryset=Gallery.objects.all()[:],
                           context_object_name='django_galleries',
                           template_name='django_galleries/index.html'
                       ), name='index'),
                       url('^(?P<pk>\d+)/$', 'django_galleries.views.gallery'),
)