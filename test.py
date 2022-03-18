import arithmos
import string

word = string.ascii_lowercase+" "+string.ascii_uppercase+" "+string.digits+" "+string.punctuation

# Encrypt
encrypted = arithmos.encrypt(word)
print("==============================")
print(encrypted)

# Decrypt
decrypted = arithmos.decrypt(encrypted)
print(decrypted)
print("==============================")
