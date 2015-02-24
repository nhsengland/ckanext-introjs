from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-introjs',
    version=version,
    description="Adds intro.js to CKAN so users can follow a guided tour of the UI",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Ano Nymous',
    author_email='ano.nymous@england.nhs.uk',
    url='https://usablica.github.io/intro.js/',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.introjs'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        # myplugin=ckanext.introjs.plugin:PluginClass
    ''',
)
