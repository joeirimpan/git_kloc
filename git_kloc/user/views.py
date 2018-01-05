# -*- coding: utf-8 -*-
"""
    user/views.py

    :copyright: (c) 2017 by Joe Paul.
    :license: see LICENSE for details.
"""
import os
from flask import (
    request, session, Blueprint, render_template, jsonify,
    url_for, redirect
)
from flask_login import login_user, logout_user, current_user
from requests_oauthlib import OAuth2Session

from .models import User

from ..extensions import login_manager


blueprint = Blueprint(
    'user', __name__, static_folder='../static'
)

GITHUB_OAUTH_URL = 'https://github.com/login/oauth/%s'


@login_manager.user_loader
def user_loader(user_id):
    if 'token' not in session:
        return
    return User(token=session['token'])


@blueprint.route('/')
def index():
    """Home page
    """
    return render_template('index.html')


@blueprint.route('/is_logged_in')
def is_logged_in():
    return jsonify(
        isLoggedIn=current_user.is_authenticated
    )


@blueprint.route('/login')
def login():
    """Login handler
    """
    github = OAuth2Session(os.environ['CLIENT_ID'])
    authorization_url, state = github.authorization_url(
        GITHUB_OAUTH_URL % 'authorize'
    )
    session['oauth_state'] = state
    return jsonify(auth_url=authorization_url)


@blueprint.route('/authorize')
def authorize():
    """Oauth2 callback route
    """
    github = OAuth2Session(
        os.environ['CLIENT_ID'],
        state=session['oauth_state']
    )
    token = github.fetch_token(
        GITHUB_OAUTH_URL % 'access_token',
        client_secret=os.environ['CLIENT_SECRET'],
        authorization_response=request.url
    )
    github.token = token
    user = User(token=token)
    session['token'] = token
    login_user(user)
    next_url = request.args.get('next') or url_for('user.index')
    return redirect(next_url)


@blueprint.route('/logout')
def logout():
    """Logout handler
    """
    session.clear()
    logout_user()
    return redirect(url_for('user.index'))
