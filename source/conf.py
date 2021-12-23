# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'oTree'
copyright = '2020, oTree team'
author = 'oTree team'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
import sys
if 'gettext' in sys.argv:

    exclude_patterns = [
        'misc/otreelite.rst',
        'misc/noself.rst',
        'misc/newconstants.rst',
        'misc/version_history.rst',
        'misc/internationalization.rst',
        'misc/django.rst',
        # for some reason, it seems I can exclude files like misc/django.rst
        # that are members of a subfolder with other files,
        # but i can't exclude a top-level file like mturk.rst, or all files within a folder.
        'mturk.rst',
        'mturk_nostudio.rst',
    ]
else:
    exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

master_doc = 'index'

locale_dirs = ["../locales/"]

#html_logo = '_static/otree-icon.png'