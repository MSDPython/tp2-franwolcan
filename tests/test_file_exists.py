import os
import pytest

def test_file_exists():
    filepath = "test.txt"
    assert os.path.isfile(filepath), f"{filepath} does not exist."
