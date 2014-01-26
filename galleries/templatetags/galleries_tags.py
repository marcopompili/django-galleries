'''
Created on 30/giu/2013

@author: Marco Pompili
'''

from django import template
from galleries.models import Gallery

register = template.Library()

class GalleryGetImagesNode(template.Node):
    """
        Returns an image set of a gallery.
        If the queryset is empty None will be returned.
    """
    def __init__(self, codename):
        try:
            gallery = Gallery.objects.get(codename=codename)
            self.images = gallery.image_set.all()
        except:
            self.images = None
    
    def render(self, context):
        context['images'] = self.images
        
        return ''
    
@register.tag()
def galleries_get_images(parser, token):
    """
        Returns the images of a given gallery.
        
        Usage::
            galleries_get_images <gallery_codename>
    """
    args = token.split_contents()
    return GalleryGetImagesNode(args[1])