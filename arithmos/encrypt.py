from .dictionary import encrypt_dict
from .errors import *

def encrypt(text:str):
    """
    A method to encrypt string to cipher.
    Return to encrypted cipher.
    ----
    Parameter :
    - text: `str` | the string to be encrypted
    """
    
    try:
        return ''.join(encrypt_dict[c] for c in list(text))
        
    except KeyError as key:
        raise UnknownKey(key)
