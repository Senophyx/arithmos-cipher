class ArithmosErrors(Exception):
    def __init__(self, message:str=None):
        if message is None:
            message = 'An unknown error has occurred within Arithmos program.'
        super().__init__(message)
        
class UnknownKey(ArithmosErrors):
    def __init__(self, key:str):
        super().__init__(f"{key} cannot be encrypted/decrypted.")

class StringIsOdd(ArithmosErrors):
    def __init__(self):
        super().__init__("String cannot be odd, must be even.")
