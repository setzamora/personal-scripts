from Crypto.Protocol.KDF import PBKDF2
from Crypto import Random
from Crypto.Hash import SHA1
import time

dictionary_file = "hash-dictionary.txt"
target_hash = "d85e382c4a48731d850ec5956a20e5b3ccaa0e7d"

ssid = ""
dklen = 32
iterations = 4096

file = open(dictionary_file, "r").read()
texts = file.split("\n")

start_time = time.time()
for text in texts:
    pbkdf2 = PBKDF2(text, ssid, dklen, iterations).hex()
    if (pbkdf2 == target_hash)
        print(text)
        break

end_time = time.time()
elapsed_time = end_time - start_time
print("Time elapsed: " + str(elapsed_time))