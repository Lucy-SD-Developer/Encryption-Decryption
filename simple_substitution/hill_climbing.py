from string import ascii_uppercase
from decryptor import decrypt_from_key
import random
import math

_RANDOM_KEY = {}
_NO_OP_CHAR = [",", ".", " ", "?"]

def get_key_by_hill_climbing(input):
    cur_fitness = None
    for i in range(0, 1000):
        key = get_random_key()
        decrypted = decrypt_from_key(input, key)
        fitness = get_fitness(decrypted)
        if not cur_fitness or fitness > cur_fitness:
            cur_fitness = fitness
            return_key = key
    return return_key


def get_fitness(input):
    # Find every quadgram in the input
    occur = []
    for i in range(0, len(input) - 4):
        quadgram = input[i:i+4]
        # Check if this substring has any no-op character
        is_valid = True
        for no_op_char in _NO_OP_CHAR:
            if no_op_char in quadgram:
                is_valid = False
                break
        if not is_valid:
            continue
        occur.append(input.count(quadgram))
    fitness = 0
    for num in occur:
        fitness = fitness + math.log((num / len(occur)))
    return fitness


def get_random_key():
    if not _RANDOM_KEY:
        return generate_random_key()
    else:
        return next_random_key()


def generate_random_key():
    key = {}
    used_cipher_text = []
    for c in ascii_uppercase:
        while True:
            i = random.randint(0, 25)
            cipher_text = chr(ord('A') + i)
            if cipher_text not in used_cipher_text:
                used_cipher_text.append(cipher_text)
                key[c] = cipher_text
                break
    return key


def next_random_key():
    # Swap two characeters in the key randomly
    i1 = random.randint(0, 25)
    i2 = random.randint(0, 25)
    c1 = chr(i1)
    c2 = chr(i2)
    temp = _RANDOM_KEY[c1]
    _RANDOM_KEY[c1] = _RANDOM_KEY[c2]
    _RANDOM_KEY[c2] = temp

