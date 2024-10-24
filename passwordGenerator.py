#!/usr/bin/env python3

import os
import string
import sys

def get_random_password(length):
    # All printable ASCII characters excluding newline and carriage return
    pool = bytearray()
    letters = bytes([ch for ch in string.ascii_letters.encode()])  # 10 is \n, 13 is \r
    digits = bytes([dg for dg in string.digits.encode()])
    punctation = bytes([pt for pt in string.punctuation.encode()])

    pool.extend(letters)
    pool.extend(digits)
    pool.extend(punctation)
    result = bytearray()
    
    while len(result) < length:
        # Generate random bytes
        random_bytes = os.urandom(length)
        # Filter for printable bytes excluding newline and carriage return
        result.extend(byte for byte in random_bytes if byte in pool)
    
    # Truncate to the desired length
    result = result[:length]
    return bytes(result)

# Usage
length = 0
if len(sys.argv) > 1:
    length = int(sys.argv[1])  # specify the length of the desired string
    print(length)
else:
    length = 16

print(f'New random password of {length * 8} bits:')

random_printable_bytes = get_random_password(length)
random_printable_string = random_printable_bytes.decode('UTF-8')
print(random_printable_string)


