# Secure Password Generator

A cryptographically secure password generator written in Python that creates strong, random passwords using proper entropy calculations and unbiased random sampling.

## Features

- **Cryptographically Secure**: Uses `os.urandom()` and `secrets` module for true randomness
- **Unbiased Sampling**: Implements rejection sampling to avoid modular bias
- **Accurate Entropy Calculation**: Provides real entropy measurements in bits
- **Flexible Length**: Generate passwords of any desired length
- **Full ASCII Support**: Uses all printable ASCII characters (letters, digits, punctuation)
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Requirements

- Python 3.3+ (for `os.urandom()`)
- Python 3.6+ recommended (for `secrets` module optimization)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/secure-password-generator.git
cd secure-password-generator
```

2. Make the script executable (Unix/Linux/macOS):
```bash
chmod +x password_generator.py
```

## Usage

### Basic Usage

Generate a 16-character password (default):
```bash
python3 password_generator.py
```

### Custom Length

Generate a password of specific length:
```bash
# 32-character password
python3 password_generator.py 32

# 8-character password  
python3 password_generator.py 8
```

### Example Output

```bash
$ python3 password_generator.py 16
Generating password of length 16
Method: secrets.choice() (recommended)
Password: K7#mR$9@pL2&vX8!
Entropy: 104.8 bits
Character set size: 94
```

## Security Features

### Character Set
- **Letters**: A-Z, a-z (52 characters)
- **Digits**: 0-9 (10 characters)  
- **Punctuation**: All ASCII punctuation (32 characters)
- **Total**: 94 printable ASCII characters

### Entropy Calculation
The entropy for each password is calculated as:
```
Entropy (bits) = length × log₂(character_set_size)
```

For our 94-character set:
- 8 characters ≈ 52.4 bits
- 12 characters ≈ 78.6 bits
- 16 characters ≈ 104.8 bits
- 20 characters ≈ 131.0 bits

### Cryptographic Security
1. **Random Source**: Uses `os.urandom()` which accesses the OS's cryptographically secure random number generator
2. **Bias Mitigation**: Implements rejection sampling to eliminate modular bias
3. **Modern Fallback**: Prefers `secrets.choice()` when available for optimal security

## Password Strength Guidelines

| Length | Entropy | Use Case |
|--------|---------|----------|
| 8-12   | 52-79 bits | Basic accounts, temporary passwords |
| 16-20  | 105-131 bits | Important accounts, standard use |
| 24+    | 157+ bits | High-security applications |

## Code Structure

```python
get_random_password(length)           # Core implementation with os.urandom()
get_random_password_efficient(length) # Optimized version using secrets module
main()                               # CLI interface and argument handling
```

## Security Considerations

- **Do not** modify the character set without understanding entropy implications
- **Store passwords securely** using proper password managers
- **Use appropriate length** for your security requirements
- **Avoid** predictable patterns or dictionary words

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## Testing

Run basic tests to verify functionality:
```bash
# Test different lengths
python3 password_generator.py 8
python3 password_generator.py 16
python3 password_generator.py 32

# Test error handling
python3 password_generator.py -1    # Should show error
python3 password_generator.py abc   # Should show error
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## References

- [NIST SP 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) - Digital Identity Guidelines
- [RFC 4086](https://tools.ietf.org/html/rfc4086) - Randomness Requirements for Security
- [Python secrets module documentation](https://docs.python.org/3/library/secrets.html)

## Changelog

### v1.0.0
- Initial release
- Cryptographically secure password generation
- Proper entropy calculations
- Cross-platform compatibility
- Command-line interface

---

**Note**: This tool generates cryptographically secure passwords suitable for production use. Always follow your organization's password policy and security guidelines.