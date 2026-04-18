class EntryRotor:
    """The entry wheel (Eintrittswaltze or EKW) is on the right of the
    Enigma. It connects the plugboard to the first rotor.

    On commercial machines it connected the key 'A' to the 'Q'
    position of the first rotor, following the German "QWERTZ"
    keyboard arrangment. On military machines, no substitution was
    done.

    For this implementation, accept an arbitrary init_string and setup
    two SubstitutionCiphers to handle the forward and reverse
    encodings.
    """

    def __init__(self, init_string):
        """
        """
        pass
        
    def rotate(self):
        """The entry rotor does not rotate. This function does nothing.
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
