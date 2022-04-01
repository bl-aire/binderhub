#!/usr/bin/env python3
#
# BinderHub documentation build configuration file, created by
# sphinx-quickstart on Tue May 16 07:17:16 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
from os.path import dirname
import sys

curdir = dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(curdir, 'script')))

# set paths
docs = dirname(dirname(__file__))
root = dirname(docs)
sys.path.insert(0, root)
sys.path.insert(0, 'sphinxext')
sys.path.insert(0, '..')

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

html_logo = "_static/images/logo.png"
html_favicon = "_static/images/favicon.png"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'autodoc_traits',
    'sphinx_copybutton',
    'myst_parser',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# Set the default role so we can use `foo` instead of ``foo``
default_role = 'literal'

# General information about the project.
project = 'BinderHub'
copyright = '2017, The Jupyter Team'
author = 'The Jupyter Team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

html_theme = 'pydata_sphinx_theme'
html_theme_options = {
  "use_edit_page_button": True,
  "github_url": "https://github.com/jupyterhub/binderhub",
  "twitter_url": "https://twitter.com/mybinderteam",
}
html_context = {
    "github_user": "jupyterhub",
    "github_repo": "binderhub",
    "github_version": "master",
    "doc_path": "doc",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'BinderHubdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'BinderHub.tex', 'BinderHub Documentation',
     'Yuvi Panda', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'binderhub', 'BinderHub Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'BinderHub', 'BinderHub Documentation',
     author, 'BinderHub', 'One line description of project.',
     'Miscellaneous'),
]


# -- Setup redirects for content that was moved internally
# each entry represent an `old` path that is now available at a `new` path
internal_redirects = [
    ("turn-off.html", "zero-to-binderhub/turn-off.html"),
    ("setup-registry.html", "zero-to-binderhub/setup-registry.html"),
    ("setup-binderhub.html", "zero-to-binderhub/setup-binderhub.html"),
    ("create-cloud-resources.html", "zero-to-binderhub/setup-prerequisites.html"),
]
internal_redirect_template = """
<!DOCTYPE html>
<html>
  <head>
    <title>Going to {new_url}</title>
    <link rel="canonical" href="{canonical_url}{new_url}"/>
    <meta name="robots" content="noindex">
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <meta http-equiv="refresh" content="0; url={new_url}"/>
  </head>
</html>
"""


def create_internal_redirects(app, docname):
    if app.builder.name in ("html", "readthedocs"):
        print(app.config['html_context'])
        canonical_url = app.config['html_context'].get("canonical_url", "")
        for old_name, new in internal_redirects:
            page = internal_redirect_template.format(
                new_url=new,
                canonical_url=canonical_url,
            )

            target_path = app.outdir + "/" + old_name
            if not os.path.exists(os.path.dirname(target_path)):
                os.makedirs(os.path.dirname(target_path))

            with open(target_path, "w") as f:
                f.write(page)


def setup(app):
    app.connect("build-finished", create_internal_redirects)
