def cycle(letter, left, right, key):
    length = ord(right) - ord(left) + 1
    return chr(
        ((ord(letter) - ord(left) + key) % length + length) % length + ord(left))
