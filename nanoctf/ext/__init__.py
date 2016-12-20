#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This package contains extra functions.
"""
from inspect import getargspec
from werkzeug.utils import import_string
from nanoctf.core.db import DB


def configure_extension(name, **kwargs):
    configurator = import_string(name)
    args = getargspec(configurator).args
    if 'db' in args and 'db' not in kwargs:
        kwargs['db'] = DB
    configurator(**{key: val for key, val in kwargs.items() if key in args})


def configure_extensions(app, admin=None):
    extensions = app.config.get(
        'CORE_EXTENSIONS', []
    ) + app.config.get(
        'EXTRA_EXTENSIONS', []
    )
    DB.init_app(app)
    for configurator_name in extensions:
        configure_extension(configurator_name, app=app, db=DB, admin=admin)
    return app
