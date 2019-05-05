from app.decode import caesar, vernam, vigenere
from tests.random_generators import generate_text, generate_binary
from tests import sizes, graphics_enabled, texts_enabled
from time import time
import numpy as np
from matplotlib import pyplot as plt


def measure_caesar():
    key = 14
    result = []
    for size in sizes:
        text = generate_text(size)
        start = time()
        caesar(text, key)
        result.append(time() - start)
    return result


def measure_vigenere():
    key = 'ababdabdjasbdasjkdbajs'
    result = []
    for size in sizes:
        text = generate_text(size)
        start = time()
        vigenere(text, key)
        result.append(time() - start)
    return result


def measure_vernam():
    key = '010101010010101010'
    result = []
    for size in sizes:
        text = generate_binary(size * 8)
        start = time()
        vernam(text, key)
        result.append(time() - start)
    return result


def test_decode_time():
    vigenere_time = measure_vigenere()
    vernam_time = measure_vernam()
    caesar_time = measure_caesar()
    if graphics_enabled:
        fig, ax = plt.subplots(1, 1, figsize=(16, 9))
        ax.plot(sizes, np.array(vigenere_time), label='vigenere')
        ax.plot(sizes, np.array(vernam_time), label='vernam')
        ax.plot(sizes, np.array(caesar_time), label='caesar')
        ax.set_xlabel('Input size')
        ax.set_ylabel('Time, s')
        ax.set_title('Mesaure time of different decode methods')
        ax.grid()
        fig.legend(loc='upper left')
        fig.savefig('test_results_images/test_decode_time.png')
    if texts_enabled:
        with open('test_results_texts/test_decode_time.txt', 'w') as file:
            file.write('Times of caesar:{}\n'.format(caesar_time))
            file.write('Times of vigenere:{}\n'.format(vigenere_time))
            file.write('Times of vernam:{}\n'.format(vernam_time))
