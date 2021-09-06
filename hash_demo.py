# Hashing demonstration from exercise 02, Section 2, Unit 18 - Blockchain

# Import the hashlib hashing function
import hashlib

# The hashlib function converts a sha256 hash into a hexidecimal fixed string format.
def hash(note):
    return hashlib.sha256(note).hexdigest()

first_note = b"This is my introduction to hash functions."
print(first_note, hash(first_note))




