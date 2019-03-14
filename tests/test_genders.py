import pytest
import project1
from project1 import redacted

def tests_genders():
    assert len(redacted.genders('Tom is my name. Bob is my friend. he visits my home always. he also visits his  dad and mom'))==5
