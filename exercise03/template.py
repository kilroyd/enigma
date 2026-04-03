def createInvertedCipher(cipher):
    """
    Return a new SubsitutionCipher which is the original cipher inverted.
    i.e. this can be used to decode text encoded by the original cipher.
    """
    return SubstitutionCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
