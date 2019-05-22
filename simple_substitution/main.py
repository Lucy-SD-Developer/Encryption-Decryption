from encryptor import encrypt
from decryptor import decrypt_from_key
from frequency import get_key_by_frequency
from hill_climbing import get_key_by_hill_climbing
from enum import Enum

test_input = "For each letter in the ciphertext, you count how many times each letter appears and then sort the list. \
According the English letter frequency table, a letter appears the most would be E, the second would be T, the third would be A, \
and so on. After replacing all letters, the ciphertext would be change back to the plaintext. \
English letter frequency method would be accurate if the ciphertext is very long. \
For short ciphertext, it may not follow the statistical rule therefore the cracked text may not accurate or not accurate at all."

class DecryptMethod(Enum):
    FREQUENCY = 1
    HILL_CLIMBING = 2
    WORD_PATTERN = 3


def decrypt(input, decrypt_method):
    if decrypt_method == DecryptMethod.FREQUENCY:
        key = get_key_by_frequency(input)
    elif decrypt_method == DecryptMethod.HILL_CLIMBING:
        key = get_key_by_hill_climbing(input)
    elif decrypt_method == DecryptMethod.WORD_PATTERN:
        raise NotImplementedError
    else:
        raise Exception("Undefined decrypt method")
    return decrypt_from_key(input, key)


if __name__ == "__main__":
    print(test_input)
    encrypted = encrypt(test_input)
    print(encrypted)
    decrypted = decrypt(encrypted, DecryptMethod.FREQUENCY)
    print(decrypted)
    decrypted = decrypt(encrypted, DecryptMethod.HILL_CLIMBING)
    print(decrypted)
