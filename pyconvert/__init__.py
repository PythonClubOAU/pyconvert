"""
Pyconvert is an all around python converter.
It will try to convert to the most acceptable standard all types of
values in a format,into another format.
It will convert :
1. Mathematical constants.
2. Files
3. Physical constants.
4. Chemical constants
"""


import sys
from pyconvert.errors import VersionError
if sys.version_info <= (2, 7):
    raise VersionError("Pyconvert requires at least python 2.7 to run")

import importlib
from pyconvert.errors import VersionError

minimum_supported_version = "2.7"
required_libraries = ["pyconvert", "tabulate", "openpyxl", "PIL"]


for lib in required_libraries:
    try:
        importlib.import_module(lib)
    except ImportError as error:
        raise ImportError(error)

