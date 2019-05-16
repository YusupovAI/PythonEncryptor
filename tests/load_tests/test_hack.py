from app.model import hack_vigenere, hack_caesar
from tests import sizes, graphics_enabled, texts_enabled
from tests.random_generators import generate_text
from tests.models import caesar_model, vigenere_model
from time import time
import numpy as np
from matplotlib import pyplot as plt


def measure_caesar():
    result = []
    for size in sizes:
        text = generate_text(size)
        start = time()
        hack_caesar(text, caesar_model, 3)
        result.append(time() - start)
    return result


def measure_vigenere():
    result = []
    for size in sizes:
        text = generate_text(size)
        start = time()
        hack_caesar(text, vigenere_model)
        result.append(time() - start)
    return result


def test_hack_time():
    vigenere_time = measure_vigenere()
    caesar_time = measure_caesar()
    if graphics_enabled:
        fig, ax = plt.subplots(1, 1, figsize=(16, 9))
        ax.plot(sizes, np.array(vigenere_time), label='vigenere')
        ax.plot(sizes, np.array(caesar_time), label='caesar')
        ax.set_xlabel('Input size')
        ax.set_ylabel('Time, s')
        ax.set_title('Mesaure time of different hack methods')
        ax.grid()
        fig.legend(loc='upper left')
        fig.savefig('test_results_images/test_hack_time.png')
    if texts_enabled:
        with open('test_results_texts/test_hack_time.txt', 'w') as file:
            file.write('Times of caesar:{}\n'.format(caesar_time))
            file.write('Times of vigenere:{}\n'.format(vigenere_time))
