from app.model import hack


class Arguments(object):
    def __init__(self, input, output, model, cipher):
        self.input = input
        self.cipher = cipher
        self.output = output
        self.model = model


def test_caesar_small():
    args = Arguments('sonnets.txt', 'out.txt', 'caesar_model.json', 'caesar')
    hack(args)


def test_caesar_large():
    args = Arguments('pg200.txt', 'out.txt', 'caesar_model.json', 'caesar')
    hack(args)


def test_vigenere_small():
    args = Arguments('sonnets.txt', 'out.txt', 'vigenere_model.json',
                     'vigenere')
    hack(args)


def test_vigenere_large():
    args = Arguments('pg200.txt', 'out.txt', 'vigenere_model.json', 'vigenere')
    hack(args)
