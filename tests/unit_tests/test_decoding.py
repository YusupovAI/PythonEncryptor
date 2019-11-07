from app.decode import caesar, vernam, vigenere
from app.to_byte import to_byte


def test_caesar_simple():
    assert caesar('bcd', 1) == 'abc'


def test_caesar_with_large_letters():
    assert caesar('zXy', 2) == 'xVw'


def test_caesar_with_symbols():
    assert caesar('; )--(', 10) == '; )--('


def test_caesar_hard():
    assert caesar('eFg ;-A', 3) == 'bCd ;-X'


def test_vigenere_simple():
    assert vigenere('bcxz', 'ba') == 'acwz'


def test_vigenere_with_large_letters():
    assert vigenere('BcxZ', 'Ba') == 'AcwZ'


def test_vigener_with_symbols():
    assert vigenere('; -0)', 'abc') == '; -0)'


def test_vigenere_hard():
    assert vigenere('xyZ a;', 'ab') == 'xxZ z;'


def test_vernam():
    assert vernam(to_byte(1), '01000000') == 'A'
