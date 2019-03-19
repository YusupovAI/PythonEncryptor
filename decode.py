import re
from cycle import cycle
from text_worker import get_stream


def caesar(args):
    key = int(args.key)

    def change(c):
        cur = str(c.group())
        if 'a' <= cur <= 'z':
            return cycle(cur, 'a', 'z', -key)
        if 'A' <= cur <= 'Z':
            return cycle(cur, 'A', 'Z', -key)

    with get_stream(args.input, 'r') as input, get_stream(args.output,
                                                          'w') as output:
        res = re.sub(r'[A-Z]|[a-z]', change, input.read())
        output.write(res)


def vigenere(args):
    pos = -1
    key = args.key.lower()

    def change(c):
        cur = str(c.group())
        nonlocal pos
        pos += 1
        if 'a' <= cur <= 'z':
            return cycle(cur, 'a', 'z', ord('a') - ord(key[pos % len(key)]))
        if 'A' <= cur <= 'Z':
            return cycle(cur, 'A', 'Z', ord('a') - ord(key[pos % len(key)]))

    with get_stream(args.input, 'r') as input, get_stream(args.output,
                                                          'w') as output:
        res = re.sub(r'[A-Z]|[a-z]', change, input.read())
        output.write(res)


def vernam(args):
    with get_stream(args.input, 'r') as input, get_stream(args.output,
                                                          'a') as output:
        pos = -1

        def chunkstring(string, length):
            return (string[0 + i:length + i] for i in
                    range(0, len(string), length))

        while len(args.key) % 7 != 0:
            args.key += '0'
        key = [int(i, 2) for i in chunkstring(args.key, 7)]

        def change(c):
            nonlocal pos
            pos += 1
            char = str(c.group())
            return chr(ord(char) ^ key[pos % len(key)])

        res = re.sub(r'[0-1]', change, input.read())
        output.write(res)


def decode(args):
    if args.cipher == 'caesar':
        caesar(args)
    elif args.cipher == 'vigenere':
        vigenere(args)
    elif args.cipher == 'vernam':
        vernam(args)
