#hashing is a one way function, you can not go the other way

import hashlib

password = "monkey100?"
data = password.encode("utf-8")
digest = hashlib.md5(data).hexdigest()
print(f"password: {password}")
print(f"hash: {digest}")

# comparing hashed passwords

diff_passwords = [ "monkey100?", "d12345678910", "d@@#hfhgj", "a","0"]

for p in diff_passwords:
    data = p.encode("utf-8") #converts plaintext to raw bytes  
    digest = hashlib.sha256(data).hexdigest()

    print(f"Password: {p}")
    print(f"Hash: {digest}", "\n")

    