"""Sphinx configuration."""
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath(".."))

project = "automata-backend"
author = "Felipe Restrepo"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]
html_static_path = ["_static"]
