from __future__ import print_function

import pytest

import ..filetypes_parser

def test_filetypes_parser(tempdir):
    tempdir.write('afile', 'some data', 'utf-8')
    with pytest.raises(OSError) as excinfo:
        filesystem.move_dir('afile', 'afile2')
    assert 'not a directory' in str(excinfo.value)