"""
MATRIX2.0
Symbol Decoder - Version 0.1

Converts numeric Unicode values back into text.
"""


def decode_values(values):
    """Convert Unicode numbers back into a string."""
    return "".join(chr(value) for value in values)


if __name__ == "__main__":
    encoded = [77, 79, 84, 72, 69, 82]
    decoded = decode_values(encoded)

    print("Encoded:", encoded)
    print("Decoded:", decoded)
