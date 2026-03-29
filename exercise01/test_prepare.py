import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import prepare

def test_prepare_lower():
    plaintext = prepare("abcdefghijklmnopqrstuvwxyz")

    assert plaintext == "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "Does not match expected plaintext"

def test_prepare_punctuation():
    plaintext = prepare("A.?!Z")

    assert plaintext == "AZ", "Does not match expected plaintext"

def test_prepare_space():
    plaintext = prepare(" A X  B ")

    assert plaintext == "AXB", "Does not match expected plaintext"
