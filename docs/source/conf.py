# coding: utf-8

import sys
import os

extensions = [
    'sphinx.ext.autodoc'
]

templates_path = ['_templates']
source_suffix = '.rst'

master_doc = 'index'

# General information about the project.
project = u'django-webdav-storage'
copyright = u'2016, Mikhail Porokhovnichenko'
author = u'Mikhail Porokhovnichenko'

# The short X.Y version.
version = u'0.7'
release = u'0.7'

language = 'en'

exclude_patterns = []

pygments_style = 'sphinx'
todo_include_todos = False

html_static_path = ['_static']

html_split_index = True
html_show_sphinx = False
html_show_copyright = False

htmlhelp_basename = 'django-webdav-storagedoc'


latex_elements = {
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'django-webdav-storage.tex', u'django-webdav-storage Documentation',
     u'Mikhail Porokhovnichenko', 'manual'),
]

man_pages = [
    (master_doc, 'django-webdav-storage', u'django-webdav-storage Documentation',
     [author], 1)
]


texinfo_documents = [
    (master_doc, 'django-webdav-storage', u'django-webdav-storage Documentation',
     author, 'django-webdav-storage', 'One line description of project.',
     'Miscellaneous'),
]
