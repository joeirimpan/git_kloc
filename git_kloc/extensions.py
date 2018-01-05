# -*- coding: utf-8 -*-
"""
    extensions.py

    :copyright: (c) 2017 by Joe Paul.
    :license: see LICENSE for details.
"""
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager


csrf_protect = CSRFProtect()
login_manager = LoginManager()
