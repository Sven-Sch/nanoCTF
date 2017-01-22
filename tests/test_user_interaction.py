# -*- coding: utf-8 -*-
"""
This TestCase provides tests for user interaction with nanoCTF `app`.

:author: Sven Sch.
"""
from flask import url_for
from pickletools import read_stringnl_noescape_pair

from tests import BaseTestCase
from nanoctf.core.dbmodel import User
import re


class BasicAppTests(BaseTestCase):
    """
    This TestCase tests whether the index page is available, the index poge is a HTML page
    """

    def test_not_successful_user_login(self):
        """
        Test successful user login.
        """
        from xml.etree.ElementTree import ElementTree
        # get response from /login (we need the CSRF token)
        response = self.client.get(url_for('security.login'))
        # get csrf token
        match = re.search(r'<input id="csrf_token" name="csrf_token" type="hidden" value="(?P<token>[a-zA-Z0-9_.-]+)">',
                          str(response.data))
        # try to login
        response = self.client.post(url_for('security.login'),
                                    data={'email': 'test@test.com',
                                          'password': 'very_secret_password',
                                          'csrf_token': match.group('token')})
        self.assert200(response)
        # TODO extend test to ensure the login was not successful
