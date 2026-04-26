class EnigmaM3:
    """Represents the military Enigma M3 machine. This has a plugboard,
    passthrough entry rotor, 3 rotors, and a fixed reflector.

    Note: we will skip the plugboard to start with.
    """

    def __init__(self, rotor_list, ukw_type, initial_pos):
        """
        rotor_list: list of the rotors to use, 'I', 'II' etc,
                   leftmost (slow) to rightmost (fast)
        ukw_type: the reflector to use, 'A', 'B', 'C' etc
        initial_pos: string containing initial rotor positions
                   leftmost (slow) ro rightmost (fast)

        The M3 uses a passthrough entry rotor.
        """
        pass

    def process(self, char):
        """Rotate the rotors first, then pass the input character through the
        sequence of ciphers.

        Return the character output by the last cipher (from the entry
        rotor).
        """
        pass
