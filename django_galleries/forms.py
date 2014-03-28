__author__ = 'Marco Pompili'

from django import forms
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _

from .models import Image

class ImageForm(forms.ModelForm):
    """
        Form used on the image admin interface.
    """
    model = Image

    as_cover = forms.NullBooleanField(widget=widgets.CheckboxInput(attrs={ 'class' : 'as_cover' }),
                                      help_text=_(u"Use this image as the cover for this gallery."),
                                      required=False)