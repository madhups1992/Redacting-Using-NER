import pytest
import project1
from project1 import redacted

def tests_date():
    assert len(redacted.date('01-12-1992 is my date of birth and my age is 26. He was born on 07 june 2000'))==2
