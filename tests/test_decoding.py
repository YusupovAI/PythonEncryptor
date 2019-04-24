from app.decode import caesar, vernam, vigenere


def test_caesar():
    assert caesar('bCd ;a', 1) == 'aBc ;z'


def test_vigenere():
    assert vigenere('xyZ a;', 'ab') == 'xxZ z;'


def test_vernam():
    assert vernam('abc', '1000000') == ''.join(
        map(lambda x: chr(ord(x) ^ 64), ['a', 'b', 'c']))
