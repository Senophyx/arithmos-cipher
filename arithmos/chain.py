from .encrypt import encrypt as EncFunc
from .decrypt import decrypt as DecFunc

class chain:
    """
    A class to chaining arithmos for more security.
    ----
    Parameter :
    - level: `int` | how many times must arithmos be encrypted (chaining).
    Classmethod :
    - encrypt
    - decrypt
    
    No return.
    """
    def __init__(self, level:int):
        self.level = level
      
    @classmethod  
    def encrypt(self, text:str):
        """
        A method to encrypt text repeatedly (based on level).
        ----
        Parameter:
        - text: `str`
        
        return encrypted cipher.
        """
        level = self.level
        enc = EncFunc(text)
        for _ in range(level):
            enc = EncFunc(enc)
        return enc
    
    @classmethod
    def decrypt(self, cipher:str):
        """
        A method to decrypt text repeatedly (based on level) until find the actual text.
        ----
        Parameter:
        - cipher: `str`
        
        return decrypted string.
        """
        cipher = str(cipher)
        level = self.level
        dec = DecFunc(cipher)
        for _ in range(level):
            dec = DecFunc(dec)
        return dec
