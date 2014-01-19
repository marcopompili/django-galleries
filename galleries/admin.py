'''
Created on 18/mag/2013

@author: Marco Pompili
'''

from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from .models import Image, Gallery

class ImageInline(AdminImageMixin, admin.StackedInline):
    model = Image
    extra = 3
    fieldsets = (
        (None, {
            'fields' : ('src',)
        }),
        ('Attributes', {
            'classes' : ('collapse',),
            'fields' : ('title', 'alt', 'description',)
        })
    )

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('codename',)
    inlines = [ImageInline]

admin.site.register(Gallery, GalleryAdmin)