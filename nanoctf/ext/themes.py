#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_themes2 import Themes


def configure(app):
    themes = Themes()
    themes.init_themes(app, app_identifier='nanoctf')
