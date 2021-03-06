#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import imp
import codecs
from setuptools import setup, find_packages

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__)))
init = os.path.join(ROOT, 'src', 'drf_querystringfilter', '__init__.py')

app = imp.load_source('drf_querystringfilter', init)

reqs = 'install.py%d.pip' % sys.version_info[0]


def read(*files):
    content = ''
    for f in files:
        content += codecs.open(os.path.join(ROOT, 'src',
                                            'requirements', f), 'r').read()
    return content


tests_requires = read('testing.pip')
dev_requires = tests_requires + read('develop.pip')
install_requires = read('install.any.pip', reqs)

readme = codecs.open('README.rst').read()
history = codecs.open('CHANGES.rst').read().replace('.. :changelog:', '')

setup(name=app.NAME,
      version=app.VERSION,
      description="""Filter backend for DjangoRestFramework able to parse url parameters""",
      long_description=readme + '\n\n' + history,
      author='Stefano Apostolico',
      author_email='s.apostolico@gmail.com',
      url='https://github.com/saxix/drf-querystringfilter',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      install_requires=install_requires,
      tests_require=dev_requires,
      extras_require={
          'dev': dev_requires,
          'test': tests_requires,
      },
      license="BSD",
      zip_safe=False,
      keywords='drf-querystringfilter',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
      ])
