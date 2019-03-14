import pytest
import project1
from project1 import redacted

def tests_read_textfiles_from_directory():
    assert len(redacted.read_textfiles_from_directory('/project/cs5293sp19-project1/project1','.txt'))>0
