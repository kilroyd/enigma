import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import alpha_rotate

def test_rotate_fwd_nowrap():
    for i in range(26):
        c = alpha_rotate('A', i)
        assert c == chr(ord('A') + i)

def test_rotate_rev_nowrap():
    for i in range(26):
        c = alpha_rotate('Z', -i)
        assert c == chr(ord('Z') - i)

def test_rotate_fwd_wrap():
    c = alpha_rotate('Z', 1)
    assert c == 'A'
    c = alpha_rotate('Y', 3)
    assert c == 'B'

def test_rotate_rev_wrap():
    c = alpha_rotate('A', -1)
    assert c == 'Z'
    c = alpha_rotate('B', -3)
    assert c == 'Y'
