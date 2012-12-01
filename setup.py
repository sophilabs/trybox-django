from setuptools import setup, find_packages

VERSION = '0.2'

setup(
    name='trybox-django',
    version=VERSION,
    description='TryBox:Django',
    author='Sophilabs',
    author_email='contact@sophilabs.com',
    url='https://github.com/sophilabs/trybox-django',
    download_url='http://github.com/sophilabs/trybox-django/tarball/trybox-django-v{0}#egg=trybox-django'.format(VERSION),
    license='MIT',
    install_requires=['django', 'trybox'],
    dependency_links=['https://github.com/sophilabs/trybox/tarball/master#egg=trybox'],
    packages=find_packages(),
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