from Crypto.Protocol.KDF import PBKDF2
from Crypto import Random
from Crypto.Hash import SHA1

plaintext = "Some plain text"
hashedtext = SHA1.new(plaintext.encode("utf-8")).hexdigest()
print (hashedtext)

