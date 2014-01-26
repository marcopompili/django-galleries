'''
Created on 24/gen/2014

@author: Marco Pompili
'''

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
      name='django-galleries',
      version='0.1',
      packages=['galleries'],
      include_package_data=True,
      license='BSD-3 License',
      description='Galleries is a simple Django app to manage image galleries.',
      long_description=README,
      url='https://github.com/marcopompili/django-galleries',
      author='Marco Pompili',
      author_email='marcs@emarcs.org',
      classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD-3 License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
      )