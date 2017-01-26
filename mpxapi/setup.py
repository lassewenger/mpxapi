from setuptools import setup, find_packages
import re

version = ''
version_re = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'

with open('mpxapi/__init__.py', 'r') as fd:
    version = re.search(version_re, fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(name='mpxapi',
      version=version,
      description='A simple library to interact with Comcast MPX platform',
      url='http://github.com/blockbuster/mpxapi',
      author='Loke Dupont / Blockbuster',
      author_email='lodu@blockbuster.dk',
      license='MIT',
      packages=find_packages(),
      install_requires=['requests'],
      zip_safe=False)