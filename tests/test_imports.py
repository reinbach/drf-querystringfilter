import pkgutil

import drf_querystringfilter as package


def test_imports():
    prefix = package.__name__ + '.'
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, prefix):
        __import__(modname, fromlist='dummy')
