""" eea.api.coremetadata Installer
"""
import os
from os.path import join
from setuptools import setup, find_packages

NAME = "eea.api.coremetadata"
PATH = NAME.split(".") + ["version.txt"]
VERSION = open(join(*PATH)).read().strip()

setup(
    name=NAME,
    version=VERSION,
    description="""An add-on for Plone to expose EEA core metadata as
    REST API endpoint""",
    long_description_content_type="text/x-rst",
    long_description=(
        open("README.rst").read() + "\n" +
        open(os.path.join("docs", "HISTORY.txt")).read()
    ),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="EEA Add-ons Plone Zope",
    author="Copernicus Team",
    author_email="mlarreategi@codesyntax.com",
    url="https://github.com/eea/eea.api.coremetadata",
    license="GPL version 2",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["eea", "eea.api"],
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7, >=3.6",
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
        "plone.dexterity",
        "plone.restapi",
        "Products.CMFPlone",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
