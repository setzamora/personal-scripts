from Crypto.Protocol.KDF import PBKDF2
from Crypto import Random
from Crypto.Hash import SHA1

plain_text = "Some plain text"
hash = SHA1.new(plain_text.encode("utf-8")).hexdigest()
print ("Plain: " + plain_text)
print ("Hash: " + hash)
