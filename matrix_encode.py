"""
MATRIX2.0
Symbol Encoder - Version 0.1

Converts text into numeric values.
"""


def encode_text(text):
    """Convert each character into its Unicode number."""
    return [ord(character) for character in text]


if __name__ == "__main__":
    message = "MOTHER"
    encoded = encode_text(message)

    print("Original:", message)
    print("Encoded:", encoded)
