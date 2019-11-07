def to_byte(number):
    res = []
    byte_length = 8
    for i in range(byte_length):
        res.append(number % 2)
        number //= 2
    return ''.join(map(str, reversed(res)))
