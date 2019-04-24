from app.model import hack_vigenere, hack_caesar
from app.encode import vigenere
import json


def test_caesar():
    with open('model_caesar.json', 'r') as file:
        assert hack_caesar('Hello', json.load(file)) == 0


# def test_vigenere():
#     with open('model_vigenere.json', 'r') as file:
#         assert hack_vigenere(vigenere(
#             "Please, call me Lenny, "
#             "I'd like to be the most popular singer all over the world!",
#             'a'),
#             json.load(file)) == 'a'
