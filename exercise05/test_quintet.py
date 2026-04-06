import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import quintet

def test_quintet_div5():
    q = quintet("ABCDEFGHIJKLMNO")
    assert q == "ABCDE FGHIJ KLMNO"

def test_quintet_empty():
    q = quintet("")
    assert q == ""

def test_quintet_rem1():
    q = quintet("LMNOPQ")
    assert q == "LMNOP Q"

def test_quintet_rem2():
    q = quintet("LMNOPQR")
    assert q == "LMNOP QR"

def test_quintet_rem3():
    q = quintet("LMNOPQRS")
    assert q == "LMNOP QRS"

def test_quintet_rem4():
    q = quintet("LMNOPQRST")
    assert q == "LMNOP QRST"
