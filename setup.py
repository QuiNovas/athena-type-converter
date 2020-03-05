from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path



# What does your project relate to?
app_keywords = 'quinovas'

# List run-time dependencies here.  These will be installed by pip when
# your project is installed. For an analysis of "install_requires" vs pip's
# requirements files see:
# https://packaging.python.org/en/latest/requirements.html
app_install_requires = []


setup(
    name='athena-type-converter',

    version='0.0.2',

    description='Helper functions to convert types returned from Athena into Python types',
    long_description='Helper functions to convert types returned from Athena into Python types',

    url='https://github.com/QuiNovas/athena-type-converter',

    author='Joseph Wortmann',
    author_email='joseph.wortmann@gmail.com',

    license='APL 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Topic :: System :: Software Distribution',

        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='quinovas',

    install_requires=[],

    package_dir={'': 'src'},
    packages=find_packages('src'),
)
