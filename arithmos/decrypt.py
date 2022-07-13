from .dictionary import decrypt_dict
import re
from .errors import *

def decrypt(cipher:str):
    """
    A method to decrypt cipher to string.
    Return decrypted string.
    ---
    Parameter :
    - cipher: `str` | cipher to be decrypted
    """
    
    if len(cipher.replace(" ", "")) % 2 == 0:
        try:
            cipher = str(cipher)
            separate = re.findall("\d{2}|\w|.|\d\s|\s+|\d$", cipher)
            decrypted = ''.join(decrypt_dict[c] for c in separate)
            return decrypted

        except KeyError as key:
            raise UnknownKey(key)
    else:
        raise StringIsOdd
