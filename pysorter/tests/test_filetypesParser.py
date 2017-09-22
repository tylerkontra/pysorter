from __future__ import print_function

import pytest
from .. import filetypesParser


def test_filetypes_file_exists():
    ftpath = "../filetypes.yaml"
    filetypesParser.filetypesParser(ftpath)


test_filetypes_file_exists()