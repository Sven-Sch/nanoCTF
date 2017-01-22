# -*- coding: utf-8 -*-
from flask_security.forms import RegisterForm, Required, StringField


class ExtendedRegisterForm(RegisterForm):
    username = StringField('Username', [Required()])
    first_name = StringField('First Name', [Required()])
    last_name = StringField('Last Name', [Required()])
