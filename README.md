django-galleries
================

Django Galleries is a simple django application to manage image galleries. Can be used with any another application, just bind the Gallery model with a foreign key to your application model. It uses the excellent sorl-thumbnail application for templating the images in the galleries.

The administration interface should be compatible with most admin themes (admin-bootstrapped, grappelli etc), not completetly sure.

Requirements
------------
- [Django >= 1.5](http://www.djangoproject.com)
- [sorl-thumbnails](https://github.com/mariocesar/sorl-thumbnail), check it out.

Installation
------------
This application can be installed using pip, cloning the repository locally and the using this command:
```
pip -e install django-galleries
```

Configuration
-------------
1. Add "galleries" to your INSTALLED_APPS setting like this (after sorl-thumbnails):
```python
INSTALLED_APPS = (
  ...
  'sorl-thumbnail',
  'django_galleries',
)
```

2. Include the galleries URLconf in your project urls.py like this:
```python
url(r'^galleries/', include('galleries.urls')),
```

<<<<<<< HEAD
3. Run `python manage.py syncdb` to create the galleries models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a gallery (you'll need the Admin app enabled).
=======
3. Run `python manage.py syncdb` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).
>>>>>>> a7916de... Update README.md

Settings
--------
settings.py parameters:
```python
GALLERY_THUMB_SIZE = '320x240'
GALLERY_SLIDESHOW = True
```

You can also use some debugging with sorl-thumbnail like this:
```python
THUMBNAIL_DEBUG = True
THUMBNAIL_COLORSPACE = None 
THUMBNAIL_FORMAT = 'PNG'
```
