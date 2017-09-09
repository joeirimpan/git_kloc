# -*- coding: utf-8 -*-
"""
    settings.py

    :copyright: (c) 2017 by Joe Paul.
    :license: see LICENSE for details.
"""
import os


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('SECRET', 'very-secret')
    DEBUG = os.environ.get('ENV', 'prod') != 'prod'


class TestConfig(Config):
    """Testing configuration"""
    TESTING = True
