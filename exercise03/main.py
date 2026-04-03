#!/usr/bin/env python3
import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import SubstitutionCipher, createInvertedCipher

cipher = SubstitutionCipher("GHIJKLMNOPQRSTUVWXYZABCDEF")
out = ""
for c in "BANANA":
    out = out + cipher.process(c)
print("ROT6(BANANA) -> {}".format(out))

cipher2 = createInvertedCipher(cipher)
out2 = ""
for c in out:
    out2 = out2 + cipher2.process(c)
print("INVROT6({}) -> {}".format(out, out2))
