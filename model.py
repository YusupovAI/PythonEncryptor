import json
import re
from text_worker import get_stream
import decode
from collections import Counter
import cycle


def train(args):
    if args.cipher == 'caesar':
        train_caesar(args)
    elif args.cipher == 'vigenere':
        train_vigenere(args)


def hack(args):
    if args.cipher == 'caesar':
        hack_caesar(args)
    elif args.cipher == 'vigenere':
        hack_vigenere(args)


def train_caesar(args):
    with open(args.model, 'w') as file, get_stream(args.input, 'r') as input:
        text = re.sub(r'[^a-z]', '', input.read().lower())
        model = Counter()
        for i in range(ord('a'), ord('z') + 1):
            model[chr(i)] = text.count(chr(i)) / len(text)
        json.dump(model, file, indent=4)


def find_key(text, model_data):
    data = []
    for i in range(ord('a'), ord('z') + 1):
        data.append((chr(i), text.count(chr(i)) / len(text)))
    best_key = 0
    best_dist = 0
    for i in range(26):
        best_dist += (data[i][1] - model_data[data[i][0]]) ** 2
    for key in range(1, 26):
        dist = 0
        for i in range(26):
            dist += (data[(i + key) % 26][1] - model_data[data[i][0]]) ** 2
        if dist < best_dist:
            best_dist, best_key = dist, key
    return best_key


def hack_caesar(args):
    with open(args.model, 'r') as file, get_stream(args.input,
                                                   'r') as input:
        model_data = json.load(file)
        text = input.read().lower()
        args.key = find_key(text, model_data)
        decode.decode(args)


def index(string):
    if len(string) < 2:
        return 0
    res = 0
    for i in range(ord('a'), ord('z') + 1):
        cnt = string.count(chr(i))
        res += cnt * (cnt - 1)
    return res / (len(string) * (len(string) - 1))


def train_vigenere(args):
    with open(args.model, 'w') as file, get_stream(args.input, 'r') as input:
        model = dict()
        text = re.sub(r'[^a-z]', '', input.read().lower())
        for i in range(ord('a'), ord('z') + 1):
            model[chr(i)] = text.count(chr(i)) / len(text)
        model['index'] = index(text)
        json.dump(model, file, indent=4)


def gcd(x, y):
    while x:
        y %= x
        x, y = y, x
    return y


def hack_vigenere(args):
    with open(args.model, 'r') as file, get_stream(args.input, 'r') as input:
        text = re.sub(r'[^a-z]', '', input.read().lower())
        length = len(text)
        current = min(length, 10000)
        model = json.load(file)
        fitted = model['index']
        i = 2
        while i < 10000:
            cur_index = 0
            for j in range(i):
                cur_index += index(text[j::i])
            if abs(cur_index / i - fitted) < 10 ** (-5):
                current = i
                break
            i += 1
        keys = []
        for i in range(current):
            keys.append(chr(find_key(text[i::current], model) + ord('a')))
        args.key = ''.join(keys)
        decode.decode(args)
