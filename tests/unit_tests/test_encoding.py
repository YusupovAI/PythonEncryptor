from app.encode import caesar
from app.encode import vigenere
from app.encode import vernam
from app.to_byte import to_byte


def test_caesar_simple():
    assert caesar('abc ', 1) == 'bcd '


def test_caesar_with_large_letters():
    assert caesar('hElLo', 3) == 'kHoOr'


def test_caesar_with_symbols():
    assert caesar(';-((00));,', 2) == ';-((00));,'


def test_caesar_hard():
    assert caesar('aBCD h;el;Lo)', 3) == 'dEFG k;ho;Or)'


def test_vigenere_simple():
    assert vigenere('kek', 'ab') == 'kfk'


def test_vigenere_with_large_letters():
    assert vigenere('BcAkDD', 'bc') == 'CeBmEF'


def test_vigenere_hard():
    assert vigenere('aBcd,  a', 'ba') == 'bBdd,  b'


def test_vernam():
    s = 'Hello '
    l = list(s)
    key = '10101010'
    answer = ''.join(map(lambda c: to_byte(ord(c) ^ int(key, 2)), l))
    assert vernam(s, key) == answer
