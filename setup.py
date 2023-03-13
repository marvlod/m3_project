from setuptools import setup, find_packages

setup(
    name='m3_project',
    version='1.0.0',
    packages=['m3_project', 'm3_project.app', 'm3_project.app.migrations', 'm3_project.m3_project'],
    url='',
    license='',
    author='vladimir',
    author_email='',
    description='grade1 test',
    install_requires=['django==2.2', 'm3-builder', 'm3-django-compat==1.9.2','m3-objectpack==2.2.47']
)
