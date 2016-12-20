#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A customized version of Flask's config module. It will load the configuration
in a specified order:

1. from an object/config file (settings.py)
"""
from flask.config import Config


class NanoctfConfig(Config):
    """
    A customized configuration object for Flask.
    """

    def load_nanoctf_config(self, config=None):
        """
        Loads the configuration of nanoCTF.

        Args:
            config: An object containing the configuration.
        """
        self.from_object(config or 'nanoctf.settings')
