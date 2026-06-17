import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import EntryRotorFactory, RotorFactory, ReflectorFactory, EntryRotor, Rotor, Reflector

def test_entry_rotor_factory():
    names = ["ABC", "QWERTZ"]
    for name in names:
        r = EntryRotorFactory(name)
        assert isinstance(r, EntryRotor)

def test_rotor_factory():
    names = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
    for name in names:
        r = RotorFactory(name, 'A')
        assert isinstance(r, Rotor)

def test_reflector_factory():
    names = ["B", "C"]
    for name in names:
        r = ReflectorFactory(name, 'A')
        assert isinstance(r, Reflector)
