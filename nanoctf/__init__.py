#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains methods to create the ``app`` object of nanoCTF.

First the app is created and the configuration is loaded. After that the core
modules will be registered to the ``app``. Finally the user modules (plugins)
will be loaded.
"""

from nanoctf.core.app import NanoctfApp
from nanoctf.ext import configure_extension, configure_extensions


def create_app_base(config=None, ext_list=None, **settings):
    """
    Creates the basic ``flask`` app and loads all core modules (listed in the
    config file). The created ``app`` will be returned.

    Args:
        config: An object containing the configuration for nanoCTF.
    Returns:
         The created ``app`` with all it's core modules.
    """
    app = NanoctfApp('nanoctf')
    app.config.load_nanoctf_config(config=config)
    if ext_list:
        for ext in ext_list:
            configure_extension(ext, app=app)
    return app


def create_app(config=None, **settings):
    app = create_app_base(config=config)
    configure_extensions(app)
    return app
