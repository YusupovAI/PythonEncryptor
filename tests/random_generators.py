import random
import string


def generate_text(length):
    return ''.join(random.choices(
        string.ascii_uppercase + string.digits + string.ascii_lowercase +
        string.punctuation + string.punctuation,
        k=length))


def generate_binary(length):
    return ''.join(random.choices(['0', '1'], k=length))
