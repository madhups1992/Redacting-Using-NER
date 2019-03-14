import pytest
import project1
from project1 import redacted

def tests_name():
    assert len(redacted.names('Tom is my name. Bob is my friend'))==2
