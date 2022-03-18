from .dictionary import decrypt_dict
import re

def decrypt(cipher:str):
    """
    A method to decrypt cipher to string
    ---
    Parameter :
    - cipher: `str` | cipher to be decrypted
    """
    
    cipher = str(cipher) # Make sure the cipher is string
    # \d{2} matches 2 digits, \w matches letters, . matches anything but latters, \d\s matches a digit followed by 1 whitespace, \s+ matches 1 or more whitespaces, \d$ matches a single digit at the end of the string
    separate = re.findall("\d{2}|\w|.|\d\s|\s+|\d$", cipher)
    decrypted = ''.join(decrypt_dict[c] for c in separate)
    return decrypted
