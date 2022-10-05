# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

from DESKey import DESKey
from DataEncryptionStandard import DataEncryptionStandard
from Utility import Utility


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Randomized hex
    plaintext = DESKey.generate_key()
    key = DESKey.generate_key()
    print("Hex Plaintext : ", plaintext)
    print("Key : ", key)

    ciphertext = DataEncryptionStandard.encrypt_hex(plaintext, key)
    print("Ciphertext : ", ciphertext)

    decrypted = DataEncryptionStandard.decrypt_hex(ciphertext, key)
    print("From decrypt process : ", decrypted)

    # string
    plaintext = "testings brow"
    key = DESKey.generate_key()
    print("String Plaintext : ", plaintext)
    print("Key : ", key)

    ciphertext = DataEncryptionStandard.encrypt_str(plaintext, key)
    print("Ciphertext : ", ciphertext)

    decrypted = DataEncryptionStandard.decrypt_str(ciphertext, key)
    print("From decrypt process : ", decrypted)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
