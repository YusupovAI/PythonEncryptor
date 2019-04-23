from encode import caesar
from encode import vigenere
from encode import vernam


def test_caesar():
    assert caesar('abc; Z ', 1) == 'bcd; A '


def test_vigenere():
    assert vigenere('aBcd,  a', 'ba') == 'bBdd,  b'


def test_vernam():
    s = 'Hello'
    l = list(s)
    key = '1010101'
    assert vernam(s, key) == ''.join(
        map(lambda c: chr(ord(c) ^ int(key, 2)), l))
