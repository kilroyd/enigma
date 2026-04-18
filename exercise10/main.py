#!/usr/bin/env python3
import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import EntryRotor

R = Reflector("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'A')
out = ""
for c in "BANANA":
    m = R.encCipher().process(c)
    R.rotate()
    out = out + m
print("BANANA == {}".format(out))
