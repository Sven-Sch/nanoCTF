#!/usr/bin/env python
# -*- coding: utf-8 -*-
from nanoctf.core.views import ContentView


def configure(app):
    # Home page
    app.add_nanoctf_url_rule('/', view_func=ContentView.as_view('home_view'))
