#!/usr/bin/env python3
import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import EnigmaM3, processMessage, quintet

plaintext = "HELLOWORLD"
M3 = EnigmaM3(["I", "II", "III"], "B", "AAA")
ciphertext = processMessage(M3, plaintext)
print("Input:    {}".format(quintet(plaintext)))
print("Output:   {}".format(quintet(ciphertext)))
print("Expected: ILBDA AMTAZ")
