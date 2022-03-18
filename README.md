[![Repo Visitors](https://visitor-badge.glitch.me/badge?page_id=LyQuid12.arithmos-cipher&left_text=Repo%20Visitors)](https://github.com/LyQuid12/arithmos-cipher)

# Arithmos Cipher
Arithmos Cipher is the most simple [Cryptography](https://en.wikipedia.org/wiki/Cryptography) that I created myself in [Python](https://python.org). Arithmos is taken from the Greek word (Arithmós or αριθμός) which means "Number".

# Explanation of how it works
Basically, the given sentences will be exchanged with numbers in alphabetical order (Example: `a = 01` to `z = 26` and `A = 27` to `Z = 52`). For numbers with one digit will be added `0` in front of it. Each one of the alphabet has a `2` digit number. And for `uppercase letters` starting from the number `27` after lowercase `(z = 26)`[.](https://youtube.com/watch?v=dQw4w9WgXcQ)

**Here the explanation :**
```
LyQuid = 382543210904

38 : L
25 : y
43 : Q
21 : u
09 : i
04 : d
```

### Packages Example
```py
import arithmos

word = "Example"

# Encrypt
encrypted = arithmos.encrypt(word)
print(encrypted)

# Decrypt
decrypted = arithmos.decrypt(encrypted)
print(decrypted)
```

## Licence & Copyright
This Project under [Apache License 2.0](https://github.com/LyQuid12/arithmos-cipher/blob/master/LICENSE).
```
Copyright (c) 2022-present LyQuid
```
