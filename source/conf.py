# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Slipchenko Group'
copyright = '2024, Slipchenko group'
author = 'Slipchenko group'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [

    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinxcontrib.bibtex',
        ]


bibtex_bibfiles = [
    'reference.bib',
    # add more BibTeX files if needed
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'


html_theme_options = {
    'navigation_depth': 3,       # Levels of TOC visible in the sidebar
    'collapse_navigation': True, # Collapse navigation entries
    'sticky_navigation': True,   # Make sidebar "sticky"
}

html_static_path = ['_static']
html_css_files = [
    'custom.css',
    'molecules.css',
]

html_js_files = [
    'custom.js',
]

#html_extra_path = ['_templates/molecules_background.html']

#html_css_files = [
#    'molecules.css',
#]
html_js_files = [
    'molecules.js',
]


