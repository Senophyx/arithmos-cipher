import arithmos
import string

word = string.ascii_lowercase+" "+string.ascii_uppercase+" "+string.digits+" "+string.punctuation

# Encrypt
encrypted = encrypt(word)
print("==============================")
print(encrypted)

# Decrypt
decrypted = decrypt(encrypted)
print(decrypted)
print("==============================")
