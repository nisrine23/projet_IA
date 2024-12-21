

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

# Informations sur le projet
project = 'projet_ia_indus'
copyright = '2024, nisrine'
author = 'nisrine'

# Extensions Sphinx
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'myst_parser',  # Support des fichiers Markdown
]
myst_enable_extensions = [
    "dollarmath",  # Mathématiques dans Markdown
    "amsmath",
    "colon_fence",  # Blocs de colonnes
]


# Chemins
templates_path = ['_templates']
exclude_patterns = []

# Thème HTML
html_theme = 'furo'
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#e91e63",  # Rose
        "color-brand-content": "#9c27b0",  # Violet
    },
    "dark_css_variables": {
        "color-brand-primary": "#f48fb1",  # Rose clair
        "color-brand-content": "#ce93d8",  # Violet clair
    },
}

# Fichiers statiques
html_static_path = ['_static']
html_css_files = ['custom.css']  # CSS personnalisé, si nécessaire

html_static_path = ['_static']
html_css_files = ['custom.css']
