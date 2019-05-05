from app.encode import encode
from app.decode import decode
import random


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


def test_vigenere_small():
    key = 'asdasd askldsanda oa ;'
    args_encode = Arguments('sonnets.txt', 'out.txt', 'vigenere', key)
    encode(args_encode)
    args_decode = Arguments('out.txt', 'tmp.txt', 'vigenere', key)
    decode(args_decode)
    with open('tmp.txt', 'r') as result, open('sonnets.txt', 'r') as answer:
        assert result.read() == answer.read()


def test_vigenere_large():
    key = 'adasd asmd, saj da f. ewjmd aksdl jk1k/k fjk; wl'
    args_encode = Arguments('pg200.txt', 'out.txt', 'vigenere', key)
    encode(args_encode)
    args_decode = Arguments('out.txt', 'tmp.txt', 'vigenere', key)
    decode(args_decode)
    with open('tmp.txt', 'r') as result, open('pg200.txt') as answer:
        assert result.read() == answer.read()


def test_vernam_small():
    key = '01001010110111010010101010101111100101'
    args_encode = Arguments('sonnets.txt', 'out.txt', 'vernam', key)
    encode(args_encode)
    args_decode = Arguments('out.txt', 'tmp.txt', 'vernam', key)
    decode(args_decode)
    with open('tmp.txt', 'r') as result, open('sonnets.txt', 'r') as answer:
        assert result.read() == answer.read()


def test_vernam_large():
    key = ''.join(random.choices(['0', '1'], k=random.randint(0, 10000)))
    args_encode = Arguments('pg200.txt', 'out.txt', 'vernam', key)
    encode(args_encode)
    args_decode = Arguments('out.txt', 'tmp.txt', 'vernam', key)
    decode(args_decode)
    with open('tmp.txt', 'r') as result, open('pg200.txt') as answer:
        assert result.read().encode('ascii',
                                    errors='ignore') == answer.read().encode(
            'ascii', errors='ignore')
