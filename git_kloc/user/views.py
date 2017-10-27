# -*- coding: utf-8 -*-
"""
    user/views.py

    :copyright: (c) 2017 by Joe Paul.
    :license: see LICENSE for details.
"""
import os
from flask import request, session, Blueprint, render_template, jsonify
from requests_oauthlib import OAuth2Session


blueprint = Blueprint(
    'user', __name__, static_folder='../static'
)

GITHUB_OAUTH_URL = 'https://github.com/login/oauth/%s'


@blueprint.route('/')
def index():
    """Home page
    """
    return render_template('index.html')


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
    session['token'] = token
    return jsonify(github.get('https://api.github.com/user').json())
