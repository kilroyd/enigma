import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import EntryRotor, SubstitutionCipher

def test_entry_rotor_enccipher():
    rotor = EntryRotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert isinstance(rotor.encCipher(), SubstitutionCipher)

def test_rotor_invcipher():
    rotor = EntryRotor("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert isinstance(rotor.invCipher(), SubstitutionCipher)
