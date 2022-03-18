import arithmos
import string
import colorgb

word = string.ascii_lowercase+" "+string.ascii_uppercase+" "+string.digits+" "+string.punctuation

# Encrypt
encrypted = arithmos.encrypt(word)
print("==============================")
print(encrypted)
print("==============================")
# Decrypt
decrypted = arithmos.decrypt(encrypted)
print(decrypted)
print("==============================")
# Checking
if decrypted == word:
   check = colorgb.fore("True", "lgreen")
else:
   check = colorgb.fore("True", "lred")

print(f"Is it same : {check}")
print("==============================")
