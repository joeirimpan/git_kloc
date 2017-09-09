# -*- coding: utf-8 -*-
"""
    manage.py

    :copyright: (c) 2017 by Joe Paul.
    :license: see LICENSE for details.
"""
from git_kloc.app import create_app


app = create_app()


if __name__ == '__main__':
    app.run()
