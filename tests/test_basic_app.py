# -*- coding: utf-8 -*-
"""
This TestCase provides some basic setup tests for the nanoCTF `app`.

:author: Sven Sch.
"""
from flask import url_for
from tests import BaseTestCase
import re


class BasicAppTests(BaseTestCase):
    """
    This TestCase tests whether the index page is available, the index poge is a HTML page
    """

    def test_is_response_code_200_on_index_page(self):
        """
        This test ensures that the index page ('/' and '/index') returns the HTTP-Status code 200.
        """
        response = self.client.get(url_for('index'))
        self.assert200(response, 'The HTTP-Status Code is not 200 on index page.')

    def test_contains_index_page_favicon(self):
        """
        This test ensures that the rendered `index.html` contains a tag for the favicon.
        """
        response = self.client.get(url_for('index'))
        match = re.search(r"<link rel=\"shortcut icon\" href=\".*favicon.ico\" />", str(response.data))
        self.assertIsNotNone(match, 'The rendered index.html page contains not the page header.')

    def test_is_test_configuration_used(self):
        """
        This test ensures that the test configuration is used for the tests.
        """
        self.assertIsNotNone(self.app.config, 'No configuration loaded')
        self.assertTrue(self.app.config['TESTING'], 'The used configuration is not the test configuration.')

    def test_is_response_code_200_on_login_page(self):
        """
        This test ensures that the login page ('/login') returns the HTTP-Status code 200.
        """
        response = self.client.get(url_for('security.login'))
        self.assert200(response, 'The HTTP-Status Code is not 200 on login page.')

    def test_is_response_code_200_on_register_page(self):
        """
        This test ensures that the register page ('/register') returns the HTTP-Status code 200.
        """
        response = self.client.get(url_for('security.register'))
        self.assert200(response, 'The HTTP-Status Code is not 200 on register page.')

    def test_is_response_code_200_on_password_reset_page(self):
        """
        This test ensures that the password reset page ('/reset') returns the HTTP-Status code 200.
        """
        response = self.client.get(url_for('security.forgot_password'))
        self.assert200(response, 'The HTTP-Status Code is not 200 on password reset page.')

    def test_is_response_code_200_on_confirm_registration_page(self):
        """
        This test ensures that the confirm registration page ('/confirm') returns the HTTP-Status code 200.
        """
        response = self.client.get(url_for('security.send_confirmation'))
        self.assert200(response, 'The HTTP-Status Code is not 200 on confirm registration page.')
