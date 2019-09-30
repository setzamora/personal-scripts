from Crypto.Protocol.KDF import PBKDF2
from Crypto import Random
from Crypto.Hash import SHA1
import time

dictionary_file = "hash-dictionary.txt"
target_hash = "d85e382c4a48731d850ec5956a20e5b3ccaa0e7d"

file = open(dictionary_file, "r").read()
texts = file.split("\n")

start_time = time.time()
for text in texts:
    utf8_text = text.encode("utf-8")
    hashed_text = SHA1.new(utf8_text).hexdigest()
    if hashed_text == target_hash:
        print("Dictionary: " + dictionary_file)
        print("Target: " + target_hash)
        print("Plain: " + text)
        break
end_time = time.time()
elapsed_time = end_time - start_time
print("Time elapsed: " + str(elapsed_time))