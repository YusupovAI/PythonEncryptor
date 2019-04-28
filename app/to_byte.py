def to_byte(n):
    res = []
    for i in range(8):
        res.append(n % 2)
        n //= 2
    return ''.join(map(str, reversed(res)))
