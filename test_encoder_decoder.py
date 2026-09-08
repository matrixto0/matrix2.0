from matrix_encode import encode_text
from matrix_decode import decode_values


def test_encode_decode():
    original = "MOTHER"

    encoded = encode_text(original)
    decoded = decode_values(encoded)

    assert decoded == original


if __name__ == "__main__":
    test_encode_decode()
    print("MATRIX2.0 encode/decode test passed.")
