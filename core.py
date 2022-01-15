from dict import *
import re

def encrypt(text:str):
    return ''.join(encrypt_dict[c] for c in list(text))

def decrypt(cipher:int):
    cipher = str(cipher)
    # \d{2} matches 2 digits, \w matches letters, \d\s matches a digit followed by 1 whitespace, \s+ matches 1 or more whitespaces, \d$ matches a single digit at the end of the string
    split_num = re.findall("\d{2}|\w|\d\s|\s+|\d$", cipher)
    decrypted = ''.join(decrypt_dict[c] for c in split_num)
    return decrypted
