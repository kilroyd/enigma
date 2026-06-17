import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import SubstitutionCipher, createInvertedCipher

def test_inverted():
    cipher1 = SubstitutionCipher("EFGHMNOPABCDIJKLUVXWYZQRST")
    cipher2 = createInvertedCipher(cipher1)
    for i in range(26):
        inp = chr(ord('A') + i)
        out1 = cipher1.process(inp)
        out2 = cipher2.process(out1)
        assert out2 == inp, "Input {} to cipher1 returned {}, decoded by cipher2 as {}".format(inp, out1, out2)

def test_inverted_passthrough():
    cipher1 = SubstitutionCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    cipher2 = createInvertedCipher(cipher1)
    for i in range(26):
        inp = chr(ord('A') + i)
        out1 = cipher1.process(inp)
        out2 = cipher2.process(out1)
        assert out2 == inp, "Input {} to cipher1 returned {}, decoded by cipher2 as {}".format(inp, out1, out2)

def test_inverted_symmetric():
    cipher1 = SubstitutionCipher("ZYXWVUTSRQPONMLKJIHGFEDCBA")
    cipher2 = createInvertedCipher(cipher1)
    for i in range(26):
        inp = chr(ord('A') + i)
        out1 = cipher1.process(inp)
        out2 = cipher2.process(out1)
        assert out2 == inp, "Input {} to cipher1 returned {}, decoded by cipher2 as {}".format(inp, out1, out2)
