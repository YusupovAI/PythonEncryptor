def to_byte(n):
    res = []
    byte_length = 8
    for i in range(byte_length):
        res.append(n % 2)
        n //= 2
    return ''.join(map(str, reversed(res)))
