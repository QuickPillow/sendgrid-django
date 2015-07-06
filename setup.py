from setuptools import setup, find_packages

import sys

__version__ = None
with open('sgbackend/version.py') as f:
    exec(f.read())

PY_VERSION = sys.version_info[0], sys.version_info[1]

if PY_VERSION < (3, 0):
    long_description = open('README.rst').read()
else:
    long_description = open('README.rst', encoding='utf-8').read()

setup(
    name='sendgrid-django',
    version=str(__version__),
    author='Yamil Asusta',
    author_email='yamil@sendgrid.com',
    url='https://github.com/elbuo8/sendgrid-django',
    packages=find_packages(),
    license='MIT',
    description='SendGrid Backend for Django',
    long_description=long_description,
    install_requires=["sendgrid==1.4.0"],
)
