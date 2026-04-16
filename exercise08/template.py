class Rotor:
    """This class represents an Enigma machine's rotor (Walzen).

    A rotor has a particular substitution that it will do, a number of
    notches that cause the next rotor in the machine to rotate
    (turnover), and a current position.

    Use two RotatingCipher classes to represent transforming an input
    character one way, and then coming back through the rotor the
    other after the signal has passed through the reflector.
    """

    def __init__(self, init_string, turnover_positions, position):
        pass

    def rotate(self):
        """Rotate one position."""
        pass

    def notch():
        """If the current position of the rotor is at a turnover position,
        return True.
        """
        pass

    def encCipher(self):
        """Return the cipher class handling the initial encoding.
        """
        pass

    def invCipher(self):
        """Return the cipher class handling the reverse encoding after it has
        passed through the reflector.
        """
        pass
