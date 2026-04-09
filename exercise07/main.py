#!/usr/bin/env python3
import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import RotatingCipher, processMessage

subst = SubstitutionCipher("NOPQRSTUVWXYZABCDEFGHIJKLM")
cipher = RotatingCipher(subst, 'N')
out = processMessage(cipher, "BANANA")
print(out)
