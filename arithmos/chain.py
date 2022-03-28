from .encrypt import encrypt as EncFunc
from .decrypt import decrypt as DecFunc

class chain:
    def __init__(self, level:int):
        self.level = level
        
    def encrypt(self, text:str):
        level = self.level
        enc = EncFunc(text)
        for _ in range(level):
            enc = EncFunc(enc)
        return enc
    
    def decrypt(self):
        level = self.level
        dec = DecFunc(text)
        for _ in range(level):
            dec = DecFunc(dec)
        return dec
