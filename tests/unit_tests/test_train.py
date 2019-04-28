from app.model import train_caesar, train_vigenere, index


def test_caesar():
    result = train_caesar('Hello')
    answer = dict()
    for char in range(ord('a'), ord('z') + 1):
        answer[chr(char)] = 0
    answer['hel'] = 1
    answer['ell'] = 1
    answer['llo'] = 1
    answer['h'] = 1 / 5
    answer['e'] = 1 / 5
    answer['l'] = 2 / 5
    answer['o'] = 1 / 5
    for key, value in result.items():
        assert abs(answer[key] - value) < 10 ** -6


def test_index():
    text = 'Braaa'
    assert abs(index(text) - (3 * 2) / (5 * 4)) < 10 ** -6


def test_index_zero():
    text = 'qwerty'
    assert index(text) == 0


def test_vigenere():
    result = train_vigenere('Goodbye')
    answer = dict()
    for char in range(ord('a'), ord('z') + 1):
        answer[chr(char)] = 0
    answer['index'] = 1 / 21
    answer['g'] = 1 / 7
    answer['o'] = 2 / 7
    answer['d'] = 1 / 7
    answer['b'] = 1 / 7
    answer['y'] = 1 / 7
    answer['e'] = 1 / 7
    for key, value in result.items():
        assert abs(answer[key] - value) < 10 ** -6
