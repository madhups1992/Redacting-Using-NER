import pytest
import project1
from project1 import redacted

def tests_name():
    assert len(redacted.address("""2136 Adipiscing Av. Lima RI 93490 #247-5577 Tincidunt St. Corpus Christi WI 97020  282-8351 Tincidunt Ave
Sedalia Utah 53700
"""))==3
