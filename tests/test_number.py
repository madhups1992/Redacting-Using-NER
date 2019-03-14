import pytest
import project1
from project1 import redacted

def tests_number():
    assert len(redacted.number('call me at (405) 397 4032. on my unavailability call me at +1 777-321-8234and my zip code is 73425'))==2
