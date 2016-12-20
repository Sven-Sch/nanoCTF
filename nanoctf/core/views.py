#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask_security.core import current_user
from nanoctf.core.templates import render_template


class ContentView(MethodView):

    def get(self):
        return render_template('index.html', current_user=current_user)
