# Encode-Decode Text in Python

This project provides a simple Python script to **encode** and **decode** messages using a custom encoding scheme. The script adds random characters as a prefix and suffix to words with three or more letters, while reversing shorter words for added obfuscation.

## Features
- **Encoding**: Adds random 3-character prefixes and suffixes to words while shifting the first letter to the end.
- **Decoding**: Removes the added random characters and restores the original word order.
- Supports **special characters, spaces, and numbers**.
- User-friendly **CLI-based interaction**.

## How It Works
### Encoding
1. Words shorter than 3 characters are reversed.
2. Words longer than 3 characters:
   - A random 3-character prefix is added.
   - The first letter moves to the end.
   - A random 3-character suffix is added.

### Decoding
1. Words shorter than 3 characters are reversed back.
2. For longer words:
   - The 3-character prefix and suffix are removed.
   - The last letter moves back to the beginning.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/encode-decode-python.git
   ```
2. Navigate to the directory:
   ```bash
   cd encode-decode-python
   ```
3. Run the script:
   ```bash
   python encode-decode.py
   ```

## Usage
1. Enter a message when prompted.
2. Choose `E` to encode or `D` to decode.
3. View the result in the terminal.

### Example
#### Encoding:
```bash
Enter your message to encode or decode: hello world
write 'E' if you want to encode and 'D' if you want to decode: E
Encoded message is: xYZellohABC pqRorldmNO
```
#### Decoding:
```bash
Enter your message to encode or decode: xYZellohABC pqRorldmNO
write 'E' if you want to encode and 'D' if you want to decode: D
Decoded message is: hello world
```

## Possible Edge Cases
- **Punctuation and special characters** remain unchanged but may affect word splitting.
- **Extra spaces** are preserved in output.
- **Already encoded messages** should not be encoded again, or they might become unrecoverable.

## Contributing
Feel free to fork this project and submit pull requests for improvements or bug fixes.

## License
This project is open-source and available under the MIT License.

