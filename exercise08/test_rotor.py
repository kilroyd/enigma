import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import Rotor, RotatingCipher
from unittest.mock import Mock

def test_rotor_enccipher():
    rotor = Rotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ", ['F'], 'A')
    assert isinstance(rotor.encCipher(), RotatingCipher)

def test_rotor_invcipher():
    rotor = Rotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ", ['F'], 'A')
    assert isinstance(rotor.invCipher(), RotatingCipher)

def test_rotor_rotate():
    rotor = Rotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ", ['F'], 'A')
    rotor.encCipher().rotate = Mock()
    rotor.invCipher().rotate = Mock()
    rotor.rotate()

    rotor.encCipher().rotate.assert_called_once()
    rotor.invCipher().rotate.assert_called_once()

def test_rotor_turnover():
    rotor = Rotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ", ['F'], 'A')
    for i in range(26):
        # Note i is zero based
        # i == 0, A
        # i == 1, B
        # i == 2, C
        # i == 3, D
        # i == 4, E
        if i == 5: # F
            assert rotor.notch(), "No turnover on {}th rotate()".format(i)
        else:
            assert rotor.notch() == False, "Unexpected turnover after {}th rotate()".format(i)
        rotor.rotate()
