from setuptools import setup, find_packages
from trybox_django import VERSION

setup(
    name='trybox-django',
    version=VERSION,
    description='TryBox:Django',
    author='Sophilabs',
    author_email='contact@sophilabs.com',
    url='https://github.com/sophilabs/trybox-django',
    download_url='http://github.com/sophilabs/trybox-django/tarball/trybox-django-v{0}#egg=trybox-django'.format(VERSION),
    license='MIT',
    install_requires = ['-e git+git://github.com/sophilabs/trybox.git'],
    packages=[
        'trybox_django',
        'trybox_django.steps',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)