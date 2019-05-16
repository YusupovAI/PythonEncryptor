from app.model import train


class Arguments(object):
    def __init__(self, istream, model, cipher):
        self.input = istream
        self.cipher = cipher
        self.model = model
        self.grams = 3


def test_caesar_small():
    args = Arguments('sonnets.txt', 'tmp.json', 'caesar')
    train(args)


def test_caesar_large():
    args = Arguments('pg200.txt', 'tmp.json', 'caesar')
    train(args)


def test_vigenere_small():
    args = Arguments('sonnets.txt', 'tmp.json', 'vigenere')
    train(args)


def test_vigenere_large():
    args = Arguments('pg200.txt', 'tmp.json', 'vigenere')
    train(args)
