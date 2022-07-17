import arithmos
import string
from time import sleep

word = string.ascii_lowercase+" "+string.ascii_uppercase+"\n"+string.digits+" "+string.punctuation

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
   check = True
else:
   check = False

print(f"Is it same : {check}")
print("==============================")
sleep(5)
