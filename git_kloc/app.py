# -*- coding: utf-8 -*-
"""
    app.py

    :copyright: (c) 2017 by Joe Paul.
    :license: see LICENSE for details.
"""
from flask import Flask
from flask_wtf.csrf import generate_csrf

from .extensions import csrf_protect
from .settings import Config


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    # register extensions
    csrf_protect.init_app(app)

    # register blueprints
    import git_kloc.user.views
    app.register_blueprint(git_kloc.user.views.blueprint)

    @app.after_request
    def set_xsrf_cookie(response):
        response.set_cookie('X-CSRF', generate_csrf())
        return response

    return app
