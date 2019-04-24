def cycle(c, left, right, key):
    length = ord(right) - ord(left) + 1
    return chr(
        ((ord(c) - ord(left) + key) % length + length) % length + ord(left))
