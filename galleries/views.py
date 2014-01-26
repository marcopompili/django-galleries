'''
Created on 12/mag/2013

@author: Marco Pompili
'''

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Gallery

def gallery(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    return render(request, 'galleries/gallery/detail.html', {
        'gallery' : gallery,
        'gallery_thumb_size' : settings.GALLERY_THUMB_SIZE,
    })