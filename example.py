import arithmos

word = "Example"

# Encrypt
encrypted = arithmos.encrypt(word)
print(encrypted)

# Decrypt
decrypted = arithmos.decrypt(encrypted)
print(decrypted)
