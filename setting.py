# -*- coding: utf-8 -*-
import os


class Config(object):
    PRO_DIR = os.path.abspath(__file__)


def obj2dict(obj):
    return {key: getattr(obj, key) for key in dir(obj) if key.isupper()}


config = obj2dict(Config)
