"""
Created on 12/mag/2013

@author: Marco Pompili
"""

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Gallery


def gallery(request, pk):
    obj = get_object_or_404(Gallery, pk=pk)
    return render(request, 'django_galleries/gallery/detail.html', {
        'gallery': obj,
        'gallery_thumb_size': settings.GALLERY_THUMB_SIZE,
    })