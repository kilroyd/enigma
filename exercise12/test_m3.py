import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import EnigmaM3, processMessage

def test_m3_rotate_right_rotor_only():
    plaintext = "HELLOWORLD"
    m3 = EnigmaM3(["I", "II", "III"], "B", "AAA")
    ciphertext = processMessage(m3, plaintext)
    assert ciphertext == "ILBDAAMTAZ"
    
def test_m3_single_rotate():
    plaintext = "HELLOWORLD"
    m3 = EnigmaM3(["III", "II", "I"], "B", "ACO")
    ciphertext = processMessage(m3, plaintext)
    assert ciphertext == "LFRYJMMJFJ"

def test_m3_double_rotate():
    plaintext = "HELLOWORLD"
    m3 = EnigmaM3(["III", "II", "I"], "B", "ADO")
    ciphertext = processMessage(m3, plaintext)
    assert ciphertext == "ARFWAZQJZR"

def test_m3_left_rotor_notch():
    plaintext = "HELLOWORLD"
    m3 = EnigmaM3(["III", "II", "I"], "B", "VAA")
    ciphertext = processMessage(m3, plaintext)
    assert ciphertext == "SNMXNTVCNR"
