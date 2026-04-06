import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import rotate

def test_rotate_fwd_nowrap():
    for i in range(26):
        c = rotate('A', i)
        assert c == chr(ord('A') + i)

def test_rotate_rev_nowrap():
    for i in range(26):
        c = rotate('Z', -i)
        assert c == chr(ord('Z') - i)

def test_rotate_fwd_wrap():
    c = rotate('Z', 1)
    assert c == 'A'
    c = rotate('Y', 3)
    assert c == 'B'

def test_rotate_rev_wrap():
    c = rotate('A', -1)
    assert c == 'Z'
    c = rotate('B', -3)
    assert c == 'Y'
