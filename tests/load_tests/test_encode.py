from app.encode import caesar, vigenere, vernam
from tests.random_generators import generate_text
import numpy as np
from matplotlib import pyplot as plt
import time
from tests import graphics_enabled, sizes, texts_enabled


def measure_caesar():
    result = []
    key = 14
    for size in sizes:
        text = generate_text(size)
        start = time.time()
        caesar(text, key)
        result.append(time.time() - start)
    return result


def measure_vigenere():
    result = []
    key = 'avsbasfsae'
    for size in sizes:
        text = generate_text(size)
        start = time.time()
        vigenere(text, key)
        result.append(time.time() - start)
    return result


def measure_vernam():
    key = '0101010100110'
    result = []
    for size in sizes:
        text = generate_text(size)
        start = time.time()
        vernam(text, key)
        result.append(time.time() - start)
    return result


def test_encode_time():
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
        ax.set_title('Mesaure time of different encode methods')
        ax.grid()
        fig.legend(loc='upper left')
        fig.savefig('test_results_images/test_encode_time.png')
    if texts_enabled:
        with open('test_results_texts/test_encode_time.txt', 'w') as file:
            file.write('Times of caesar:{}\n'.format(caesar_time))
            file.write('Times of vigenere:{}\n'.format(vigenere_time))
            file.write('Times of vernam:{}\n'.format(vernam_time))
