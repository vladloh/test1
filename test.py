import pytest
from classes import Autocompletor
import random
import string


def rnd(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))


def test_1():
    autocompletor = Autocompletor()
    autocompletor.build_dictionary()
    tokens = ["Sister", "Inclus", "Ufck", "Degen", "Memas", "neigh"]
    for _ in range(100):
        tokens.append(rnd(1))

    for _ in range(1000):
        tokens.append(rnd(2))

    for _ in range(1000):
        tokens.append(rnd(3))

    for _ in range(1000):
        tokens.append(rnd(4))

    for word in tokens:
        result = autocompletor.search_top_k_strings(word)
        expected_result = autocompletor.search_top_k_strings(word)
        assert result == expected_result
