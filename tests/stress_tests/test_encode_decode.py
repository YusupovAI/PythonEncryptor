from app import decode, encode
import string
import random


def generate_text():
    return ''.join(random.choices(
        string.ascii_uppercase + string.digits + string.ascii_lowercase +
        string.punctuation + string.punctuation,
        k=random.randint(0, 10 ** 5)))


def test_caesar():
    for i in range(100):
        text = generate_text()
        key = random.randint(0, 10000)
        assert decode.caesar(encode.caesar(text, key), key) == text


def test_vigenere():
    for i in range(100):
        text = generate_text()
        key = ''.join(
            random.choices(string.ascii_lowercase + string.ascii_uppercase,
                           k=random.randint(0, 10000)))
        assert decode.vigenere(encode.vigenere(text, key), key) == text


def test_vernam():
    for i in range(100):
        text = generate_text()
        key = ''.join(random.choices(['0', '1'], k=random.randint(0, 10000)))
        assert decode.vernam(encode.vernam(text, key), key) == text
