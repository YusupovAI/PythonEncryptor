import json
import re
from app.text_worker import get_stream
from app import decode, cycle
from collections import Counter


def train(args):
    with open(args.model, 'w') as file, get_stream(args.input, 'r') as input:
        if args.cipher == 'caesar':
            json.dump(train_caesar(input.read()), file, indent=4)
        elif args.cipher == 'vigenere':
            json.dump(train_vigenere(input.read()), file, indent=4)


def hack(args):
    with open(args.model, 'r') as file, get_stream(args.input, 'r') as input:
        if args.cipher == 'caesar':
            args.key = hack_caesar(input.read(), json.load(file))
            decode.decode(args)
        elif args.cipher == 'vigenere':
            args.key = hack_vigenere(input.read(), json.load(file))
            decode.decode(args)


def train_caesar(text):
    text = text.lower()
    model = Counter()
    for i in range(ord('a'), ord('z') + 1):
        model[chr(i)] = text.count(chr(i)) / len(text)

    for i in range(len(text) - 2):
        cur = text[i:i + 3]
        if cur.isalpha():
            model[cur] += 1
    return model


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


def hack_caesar(text, model_data):
    text = text.lower()
    if len(text) > 1000:
        return find_key(text, model_data)
    else:
        best_probability = 0
        best_key = 0
        for i in range(26):
            probability = 0

            def change(char):
                cur = str(char.group())
                return cycle.cycle(cur, 'a', 'z', -i)

            for j in range(len(text) - 2):
                cur = text[j:j + 3]
                if cur.isalpha():
                    cur = re.sub(r'[a-z]', change, cur)
                    probability += model_data[
                        cur] if cur in model_data else 0
            if probability >= best_probability:
                best_key = i
                best_probability = probability
        return best_key


def index(string):
    if len(string) < 2:
        return 0
    res = 0
    for i in range(ord('a'), ord('z') + 1):
        cnt = string.count(chr(i))
        res += cnt * (cnt - 1)
    return res / (len(string) * (len(string) - 1))


def train_vigenere(text):
    model = dict()
    text = re.sub(r'[^a-z]', '', text.lower())
    for i in range(ord('a'), ord('z') + 1):
        model[chr(i)] = text.count(chr(i)) / len(text)
    model['index'] = index(text)
    return model


def hack_vigenere(text, model):
    text = re.sub(r'[^a-z]', '', text.lower())
    length = len(text)
    fitted = model['index']
    i = min(length // 10, 100)
    best_diff = 10000
    best_len = 0

    while i > 0:
        cur_index = 0
        for j in range(i):
            cur_index += index(text[j::i])
        if abs(cur_index / i - fitted) < best_diff + 10 ** -3:
            best_diff = abs(cur_index / i - fitted)
            best_len = i
        i -= 1
    keys = []
    for i in range(best_len):
        keys.append(chr(find_key(text[i::best_len], model) + ord('a')))
    return ''.join(keys)
