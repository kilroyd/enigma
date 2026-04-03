import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import SubstitutionCipher

def test_substitution_cipher_symmetric():
    # This cipher is symmetric. Encoding it twice should give us back the original
    cipher = SubstitutionCipher("ZYXWVUTSRQPONMLKJIHGFEDCBA")
    message = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
    for c in message:
        out = cipher.process(c)
        second = cipher.process(out)
        assert(c == second)

def test_substitution_cipher():
    init = "QWERTYUIOPASDFGHJKLZXCVBNM"
    cipher = SubstitutionCipher(init)
    message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, c in enumerate(message):
        out = cipher.process(c)
        assert(out == init[i])
