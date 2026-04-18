class Reflector:
    """The reflector (Umkehrwalze or UKW) is on the left of the Enigma. It
    takes the output of the last rotor and feeds it back into the
    rotor in the other direction. Following the signal through the
    rotors in the other direction requires using the inverse
    substitutions.
    """

    def __init__(self, init_string, position='A'):
        """The reflector wires one output from the last rotor to another of
        the outputs on the same rotor. It is therefore self-reciprocal
        i.e. if 'A' translates to 'G', then 'G' must translate to 'A'.

        The reflector is allowed to be set in a different position on
        some models. Commercial Model C allows two
        positions. Commercial Model D allows 26 positions. The
        reflector does not rotate in these models.
        """
        pass

    def rotate(self):
        """The reflector does not rotate. This function does nothing.
        """
        pass

    def encCipher(self):
        """Return the cipher class handling the initial encoding.
        """
        pass

    def invCipher(self):
        """The reflector should always return None for the inverse cipher.
        """
        return None
