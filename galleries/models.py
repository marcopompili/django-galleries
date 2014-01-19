'''
Created on 06/mag/2013

@author: Marco Pompili
'''

from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField

class Gallery(models.Model):
    class Meta:
        verbose_name = _(u"gallery")
        verbose_name_plural = _(u"galleries")
        
    codename = models.CharField(max_length=25, unique=True, help_text=_(u"The codename is useful for the administration panel and for the slider tag."))
    
    title = models.CharField(max_length=75, blank=True, null=True, help_text=_(u"The title is optional."))
    
    def __unicode__(self):
        return self.title if self.title else self.codename

class Image(models.Model):
    class Meta:
        verbose_name = _(u"image")
        verbose_name_plural = _(u"images")
    
    src = ImageField(upload_to='images/', verbose_name=_(u"Image file"))
    title = models.CharField(max_length=75, blank=True, null=True)
    alt = models.CharField(max_length=50, blank=True, null=True)
    
    description = models.CharField(max_length=100, blank=True, null=True)
    gallery = models.ForeignKey(Gallery)
    
    def __unicode__(self):
        return self.title if self.title else self.src