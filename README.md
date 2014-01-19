django-galleries
================

Galleries is a simple Django app to manage image galleries.

Requirements
------------
- [Django >= 1.5](http://www.djangoproject.com)
- [sorl-thumbnails](https://github.com/mariocesar/sorl-thumbnail)

Quick start
-----------

1. Add "galleries" to your INSTALLED_APPS setting like this:
```python
INSTALLED_APPS = (
  ...
  'galleries',
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

5. Visit http://127.0.0.1:8000/galleries/ to check the gallery list.


Notes
----
Settings parameters:

GALLERY_THUMB_SIZE

GALLERY_SLIDESHOW
