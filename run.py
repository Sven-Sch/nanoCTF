#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script is just for testing purpose to start nanoCTF.
"""
import nanoctf


def pretty(d, indent):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))


#
#   Just for testing
#
app = nanoctf.create_app()
app.run()
