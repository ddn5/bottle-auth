#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

description = "Bootle authentication, for Personal, Google, Twitter and "\
    "facebook."

setup(
    name='bottle-auth',
    version="0.3.1",
    description=description,
    author="Thiago Avelino",
    author_email="thiago@avelino.xxx",
    url='https://github.com/avelino/bottle-auth',

    package_dir={'bottle_auth': 'bottle_auth'},

    install_requires=['webob==1.3.1', 'bottle>=0.9', 'bottle-mongo==0.2.2',
                      'bottle-beaker==0.1.0'],
    classifiers=[
        'Environment :: Web Environment',
        'Environment :: Plugins',
        'Framework :: Bottle',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
