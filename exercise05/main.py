#!/usr/bin/env python3
import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import *

cipher = SubstitutionCipher("NOPQRSTUVWXYZABCDEFGHIJKLM")
out = processMessage(cipher, "BANANA")
print("ROT13(BANANA) -> {}".format(quintet(out)))
