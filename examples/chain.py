import arithmos

# Variables
chain = arithmos.chain(level=3) # 3 is hard enough to decrypt.
# Level is up to you. bigger number = more hard to decrypt, but takes a long time to encrypt.
word = "Example"

# Encrypt
encrypted = chain.encrypt(word)
print(encrypted)

# Decrypt
decrypted = chain.decrypt(encrypted)
print(decrypted)
