"""
Created on 06/mag/2013

@author: Marco Pompili
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField


class Gallery(models.Model):
    """
        Gallery model for the Django Gallery application.
    """
    class Meta:
        verbose_name = _(u'gallery')
        verbose_name_plural = _(u'galleries')

    codename = models.CharField(max_length=25, unique=True, help_text=_(
        u'The codename is useful for the administration panel and for the slider tag.'))

    title = models.CharField(max_length=75, blank=True, null=True, help_text=_(u'The title is optional.'))

    def __unicode__(self):
        return self.title if self.title else self.codename


class Image(models.Model):
    """
        Image mode for the Django Gallery application.
        This model basically store al the attributes of an img tag
        and add a few custom options like caption.
    """
    class Meta:
        verbose_name = _(u'image')
        verbose_name_plural = _(u'images')

    src = ImageField(upload_to='images/', verbose_name=_(u'Image file'))

    title = models.CharField(_(u'Title'), max_length=75, blank=True, null=True,
                             help_text=_(u"Value for the title attribute."))

    alt = models.CharField(_(u'Alt'), max_length=50, blank=True, null=True,
                           help_text=_(u'Value for the "alt" attribute, useful if an image is not displayed.'))

    caption = models.TextField(_(u'Caption'), max_length=250, blank=True, null=True,
                               help_text=_(u"The description for this image, displayed usually under the image."))

    gallery = models.ForeignKey(Gallery, verbose_name=_(u'Gallery'))

    as_cover = models.NullBooleanField(_(u'Use as cover'), blank=True, null=True,
                                       help_text=_(u"Use this image as the cover for this gallery."))

    def __unicode__(self):
        return self.title if self.title else self.src