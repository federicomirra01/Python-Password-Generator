#!/usr/bin/env python3
import os
import string
import sys
import math

def get_random_password(length):
    """Generate a cryptographically secure random password."""
    # Define character pool
    chars = string.ascii_letters + string.digits + string.punctuation
    pool_size = len(chars)
    
    # Calculate actual entropy
    entropy_bits = length * math.log2(pool_size)
    
    password = []
    
    # Use rejection sampling with proper bounds
    max_valid = (256 // pool_size) * pool_size  # Largest multiple of pool_size ≤ 256
    
    while len(password) < length:
        # Generate one random byte at a time
        byte_val = ord(os.urandom(1))
        
        # Only use if it's in the unbiased range
        if byte_val < max_valid:
            password.append(chars[byte_val % pool_size])
    
    return ''.join(password), entropy_bits

def get_random_password_efficient(length):
    """More efficient version using secrets module (Python 3.6+)."""
    import secrets
    chars = string.ascii_letters + string.digits + string.punctuation
    entropy_bits = length * math.log2(len(chars))
    
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password, entropy_bits

# Usage
def main():
    length = 16  # default
    
    if len(sys.argv) > 1:
        try:
            length = int(sys.argv[1])
            if length <= 0:
                print("Error: Password length must be positive")
                sys.exit(1)
        except ValueError:
            print("Error: Invalid length argument")
            sys.exit(1)
    
    print(f"Generating password of length {length}")
    
    # Use the more efficient version if available
    try:
        password, entropy = get_random_password_efficient(length)
        print(f"Method: secrets.choice() (recommended)")
    except ImportError:
        password, entropy = get_random_password(length)
        print(f"Method: os.urandom() with rejection sampling")
    
    print(f"Password: {password}")
    print(f"Entropy: {entropy:.1f} bits")
    print(f"Character set size: {len(string.ascii_letters + string.digits + string.punctuation)}")

if __name__ == "__main__":
    main()