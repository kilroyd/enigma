import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import SubstitutionCipher, RotatingCipher
from unittest.mock import Mock, call

def test_rotating_cipher():
    init = "QWERTYUIOPASDFGHJKLZXCVBNM"
    cipher = SubstitutionCipher(init)
    rot_cipher = RotatingCipher(cipher, 'A')
    message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, c in enumerate(message):
        out = rot_cipher.process(c)
        assert(out == init[i])
    rot_cipher.rotate()
    for i, c in enumerate(message):
        out = rot_cipher.process(c)
        if c == 'Z':
            assert out == chr(ord(init[0])-1)
        elif out == 'Z':
            assert init[i+1] == 'A'
        else:
            assert out == chr(ord(init[i+1])-1)

def test_rotating_cipher_mock():
    cipher = SubstitutionCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    cipher.process = Mock(return_value='N')
    rot_cipher = RotatingCipher(cipher, 'A')
    out_seq = ""
    for i in range(26):
        out = rot_cipher.process('A')
        out_seq = out_seq + out
        rot_cipher.rotate()
    assert out_seq == "NMLKJIHGFEDCBAZYXWVUTSRQPO"
    expected = [call('A'),
                call('B'),
                call('C'),
                call('D'),
                call('E'),
                call('F'),
                call('G'),
                call('H'),
                call('I'),
                call('J'),
                call('K'),
                call('L'),
                call('M'),
                call('N'),
                call('O'),
                call('P'),
                call('Q'),
                call('R'),
                call('S'),
                call('T'),
                call('U'),
                call('V'),
                call('W'),
                call('X'),
                call('Y'),
                call('Z')]
    assert cipher.process.call_args_list == expected
