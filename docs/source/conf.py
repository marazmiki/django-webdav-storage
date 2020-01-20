extensions = [
    'sphinx.ext.autodoc'
]

templates_path = ['_templates']
source_suffix = '.rst'

master_doc = 'index'

# General information about the project.
project = 'django-webdav-storage'
copyright = u'2017, Mikhail Porokhovnichenko'
author = 'Mikhail Porokhovnichenko'

# The short X.Y version.
version = u'1.0'
release = u'1.0'

language = 'en'

exclude_patterns = []

pygments_style = 'sphinx'
todo_include_todos = False

html_static_path = ['_static']

html_split_index = True
html_show_sphinx = False
html_show_copyright = False
htmlhelp_basename = 'django-webdav-storagedoc'
