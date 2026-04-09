class RotatingCipher:
    """This class represents a cipher that shifts as it does in Enigma.

    Keep calling process() to do substitutions in the current
    position. Call rotate() to change the position.
    """

    def __init__(self, cipher, position):
        """
        cipher - will be a SubstitutionCipher

        position - the character that displays in the window in this position
        """
        pass

    def process(self, char):
        """When in the initial position, 'A', the substition cipher will
        operate normally.

        When moved to position 'B', an input of 'A' is seen on the
        rotor as 'B'. Say the output is 'G'. Because the whole rotor
        has moved, this output is actually at the physical location of
        'F', so we need to adjust the output too.

        This returns the encoded character.
        """
        pass

    def rotate(self):
        """
        Rotate one position. Reset to 'A' when we go past 'Z'

        There is no return value.
        """
        pass
