# salting_demo.py
# Salt: random bytes added to a password before hashing.
# Same password + different salt -> different hash.

import hashlib
import os

plaintext_password = "monkey100?"
password = plaintext_password.encode("utf-8") # pw converted into bytes

#1 no salt: two users, same password -> identical hashes (easy to spot/crack)
hash_a = hashlib.sha256(password).hexdigest()
hash_b = hashlib.sha256(password).hexdigest()

print("No salt:")
print(f"  User A: {hash_a}")
print(f"  User B: {hash_b}")

# 2 With salt: each user gets their own random salt -> different hashes
salt_a = os.urandom(16)
salt_b = os.urandom(16)

print(f"user A salt: {salt_a}")
print(f"user B salt: {salt_b}")

salt_hash_a = hashlib.sha256(salt_a + password).hexdigest()
salt_hash_b = hashlib.sha256(salt_b + password).hexdigest()

print("\n --With salt--")
print(f"User A hash(with salt): {salt_hash_a}")
print(f"User B hash(with salt): {salt_hash_b}")