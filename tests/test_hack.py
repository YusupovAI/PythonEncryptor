from app.model import hack_vigenere, hack_caesar
from app.encode import vigenere
import json


def test_caesar():
    with open('model_caesar.json', 'r') as file:
        assert hack_caesar('Hello', json.load(file)) == 0


