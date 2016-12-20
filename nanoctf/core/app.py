#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the most important part of nanoCTF, the `NanoctfApp` and
`NanoctfModule` class.
"""

import flask
import nanoctf.core.config


class NanoctfApp(flask.Flask):
    """
    This app class extends and customizes ``Flask``. It is the responsible for
    handling all HTTP requests. This includes the requests to modules,
    because the `NanoctfModule` will be registered to this app.
    """
    config_class = nanoctf.core.config.NanoctfConfig

    def add_nanoctf_url_rule(self, rule, endpoint=None,
                             view_func=None, **options):
        if endpoint is None:
            endpoint = flask.helpers._endpoint_from_view_func(view_func)
        if not endpoint.startswith('nanoctf.'):
            endpoint = 'nanoctf.core.' + endpoint
        self.add_url_rule(rule, endpoint, view_func, **options)


class NanoctfModule(flask.Blueprint):
    """
    The base module class for nanoCTF. Each module should extend this class.
    """

    def __init__(self, name, *args, **kwargs):
        name = "nanoctf.modules." + name
        super(NanoctfModule, self).__init__(name, *args, **kwargs)
