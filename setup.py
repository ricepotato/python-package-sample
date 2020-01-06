# -*- coding: utf-8 -*-

import sys
import setuptools
import configparser
from setuptools import setup

config = configparser.ConfigParser()
config.read('package.ini')
section = config["smplsvc"]

setup(name=section["name"],
      version=section["version"],
      author=section["author"],
      author_email=section["author_email"],
      url=section["url"],
      packages=setuptools.find_packages()
      )
