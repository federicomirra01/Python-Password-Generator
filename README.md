# Random Password Generator
This repository contains a Python script that generates secure, random passwords made up of printable ASCII characters, including letters, digits, and punctuation.

Features:
- Customizable Length: Specify the desired length for the password. Defaults to 16 characters if no length is provided.
- Character Set: Includes uppercase and lowercase letters, digits, and punctuation symbols.
- Cryptographic Security: Uses os.urandom() for cryptographically secure random bytes, ensuring high entropy suitable for security applications.
- Excludes Non-printable Characters: Avoids characters like newline (\n) and carriage return (\r), ensuring the password is fully printable.
