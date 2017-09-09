# -*- coding: utf-8 -*-
"""
    user/views.py

    :copyright: (c) 2017 by Joe Paul.
    :license: see LICENSE for details.
"""
from flask import Blueprint, render_template


blueprint = Blueprint(
    'user', __name__,
    url_prefix='/', static_folder='../static'
)


@blueprint.route('/', methods=["GET", "POST"])
def index():
    """
    Home page
    """
    return render_template('index.html')
