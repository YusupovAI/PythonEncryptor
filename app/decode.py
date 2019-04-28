import re
from app.cycle import cycle
from app.text_worker import get_stream


def caesar(text, key):
    def change(c):
        cur = str(c.group())
        if 'a' <= cur <= 'z':
            return cycle(cur, 'a', 'z', -key)
        if 'A' <= cur <= 'Z':
            return cycle(cur, 'A', 'Z', -key)

    res = re.sub(r'[A-Z]|[a-z]', change, text)
    return res


def vigenere(text, key):
    pos = -1
    key = key.lower()
    key = re.sub(r'[^a-z]', '', key)

    def change(c):
        cur = str(c.group())
        nonlocal pos
        pos += 1
        if 'a' <= cur <= 'z':
            return cycle(cur, 'a', 'z', ord('a') - ord(key[pos % len(key)]))
        if 'A' <= cur <= 'Z':
            return cycle(cur, 'A', 'Z', ord('a') - ord(key[pos % len(key)]))

    res = re.sub(r'[A-Z]|[a-z]', change, text)
    return res


def vernam(text, key):
    pos = -1

    def chunk_string(string, length):
        return (string[0 + i:length + i] for i in
                range(0, len(string), length))

    while len(key) % 8 != 0:
        key += '0'
    key = [int(i, 2) for i in chunk_string(key, 8)]

    def change(c):
        nonlocal pos
        cur = int(c, 2)
        pos += 1
        return chr(cur ^ key[pos % len(key)])

    res = ''.join(map(change, chunk_string(text, 8)))

    return res


def decode(args):
    with get_stream(args.input, 'r') as input, get_stream(args.output,
                                                          'w') as output:
        if args.cipher == 'caesar':
            output.write(caesar(input.read(), int(args.key)))
        elif args.cipher == 'vigenere':
            output.write(vigenere(input.read(), args.key))
        elif args.cipher == 'vernam':
            output.write(
                vernam(input.read(), args.key))
