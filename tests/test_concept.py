import pytest
import project1
from project1 import redacted

def tests_concept():
    assert len(redacted.concepts("""Tom is my name. 
    Bob is a friend. 
    i am good. 
    
    i bought an apple for free.
    am happy
    we all are doing well.
    \n please consider us.\n They are cruel""",'good'))==2
