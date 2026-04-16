#!/usr/bin/env python3
import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import Rotor

R1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", ['Q'], 'A')
out = ""
for c in "BANANA":
    m = R1.encCipher().process(c)
    n = R1.invCipher().process(m)
    R1.rotate()
    notch = R1.notch()
    out = out + n
print("BANANA == {}".format(out))
