from .dictionary import *

def encrypt(text:str):
    """
    A method to encrypt string to Arithmos
    ----
    Parameter :
    - text: `str` | the string to be encrypted
    """

    return ''.join(encrypt_dict[c] for c in list(text))