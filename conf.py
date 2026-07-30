Python
project = 'communities-anywhere'
copyright = '2026'
author = 'Admin'

extensions = [ 'sphinx.ext.autodoc',
               'sphinx.ext.napoleon',
               'sphinx_sitemap',
              ]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster' # Screenshot wala classic white theme


# Meta Tags Configuration
html_context = {
    'metatags': '''
        <meta name="description" content="Learn how to activate Bitdefender Ultimate Security with your license key fast; plus fixes for 'code not working' errors. For any issue visit official website">
        <meta name="Activate Bitdefender Ultimate Security" content="docs, guide, setup, tutorial">
     
    '''
}
