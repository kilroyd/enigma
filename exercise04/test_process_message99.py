import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import SubstitutionCipher, processMessage
from unittest.mock import Mock, call

def test_process_message():
    text = "ABRACADABRA"
    cipher = SubstitutionCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    cipher.process = Mock(return_value='x')
    out = processMessage(cipher, text)
    expected = [call('A'),
                call('B'),
                call('R'),
                call('A'),
                call('C'),
                call('A'),
                call('D'),
                call('A'),
                call('B'),
                call('R'),
                call('A')]
    assert cipher.process.call_args_list == expected
    assert out == "xxxxxxxxxxx"
