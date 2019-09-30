from Crypto.Protocol.KDF import PBKDF2
from Crypto import Random
from Crypto.Hash import SHA1
import time

targethash = "d85e382c4a48731d850ec5956a20e5b3ccaa0e7d"

file = open("dictionary.txt", "r").read()
texts = file.split("\n")

now = time.time()
for text in texts:
    utf8text = text.encode("utf-8")
    hashedtext = SHA1.new(utf8text).hexdigest()
    if hashedtext == targethash:
        print(text)
        break

elapsedtime = (time.time() - now)
print("Time elapsed: " + str(elapsedtime))

