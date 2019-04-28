from app.encode import encode
from app.decode import decode


class Arguments(object):
    def __init__(self, input, output, cipher, key):
        self.input = input
        self.output = output
        self.cipher = cipher
        self.key = key


def test_caesar_small():
    args_encode = Arguments('sonnets.txt', 'out.txt', 'caesar', '25')
    encode(args_encode)
    args_decode = Arguments('out.txt', 'tmp.txt', 'caesar', '25')
    decode(args_decode)
    with open('tmp.txt', 'r') as result, open('sonnets.txt', 'r') as answer:
        assert result.read() == answer.read()


def test_caesar_large():
    args_encode = Arguments('pg200.txt', 'out.txt', 'caesar', '20')
    encode(args_encode)
    args_decode = Arguments('out.txt', 'tmp.txt', 'caesar', '20')
    decode(args_decode)
    with open('tmp.txt', 'r') as result, open('pg200.txt') as answer:
        assert result.read() == answer.read()
