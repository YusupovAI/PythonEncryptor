from app.model import hack_vigenere, hack_caesar
from app.encode import vigenere
import json
from tests.models import caesar_model, vigenere_model


def test_caesar():
    assert hack_caesar('Hello', caesar_model) == 0

# def test_vigenere():
#     with open('model_vigenere.json', 'r') as file:
#         assert hack_vigenere(vigenere(
#             "Please, call me Lenny, "
#             "I'd like to be the most popular singer all over the world!",
#             'a'),
#             json.load(file)) == 'a'
