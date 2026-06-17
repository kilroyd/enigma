import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import Reflector, RotatingCipher
from unittest.mock import Mock

def test_reflector_enccipher():
    rotor = Reflector("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 'A')
    assert isinstance(rotor.encCipher(), RotatingCipher)

def test_reflector_invcipher():
    rotor = Reflector("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 'A')
    assert rotor.invCipher() is None

def test_reflector_rotate():
    rotor = Reflector("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 'A')
    rotor.encCipher().rotate = Mock()
    rotor.rotate()

    rotor.encCipher().rotate.assert_not_called()
