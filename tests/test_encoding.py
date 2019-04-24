from app.encode import caesar
from app.encode import vigenere
from app.encode import vernam


def test_caesar_simple():
    assert caesar('abc ', 1) == 'bcd '


def test_caesar_with_symbols():
    assert caesar(';ad;;asz ,', 2) == ';cf;;cub ,'


def test_vigenere():
    assert vigenere('aBcd,  a', 'ba') == 'bBdd,  b'


def test_vernam():
    s = 'Hello'
    l = list(s)
    key = '1010101'
    assert vernam(s, key) == ''.join(
        map(lambda c: chr(ord(c) ^ int(key, 2)), l))
