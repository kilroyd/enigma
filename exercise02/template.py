
# This file is a skeleton to be copied from in exercise02

# Copy this class to your src/enigma.py, and complete it
class SubstitutionCipher:
    """This class encapsulates the behavior we need for a simple
    substition cipher. This is where each letter is replaced by
    another specific letter.

    We must be able to handle every possible input letter.

    This can be used to implement simple rotation ciphers e.g. ROT13
    """

    def __init__(self, init_string):
        """
        init_string - describes the substitution to perform. The string is
                      a list of the encoded letters. Find the input letter
                      in the string "ABCDEFGHIJKLMNOPQRSTUVWXYZ". The
                      encoded letter is the letter in the same position in
                      init_string.
        """
        pass

    def process(self, char):
        """
        char - the input letter

        This function will return the encoded letter.
        """
        pass
