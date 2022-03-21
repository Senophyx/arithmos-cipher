from .dictionary import encrypt_dict

def encrypt(text:str):
    """
    A method to encrypt string to cipher.
    Return to encrypted cipher.
    ----
    Parameter :
    - text: `str` | the string to be encrypted
    """

    return ''.join(encrypt_dict[c] for c in list(text))
