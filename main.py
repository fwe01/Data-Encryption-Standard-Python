import secrets

from Key import Key
from DataEncryptionStandard import DataEncryptionStandard

if __name__ == '__main__':
    # Randomized hex
    plaintext = Key.generate_key()
    key = Key.generate_key()
    print("Hex Plaintext : ", plaintext)
    print("Key : ", key)

    ciphertext = DataEncryptionStandard.encrypt_hex(plaintext, key)
    print("Ciphertext : ", ciphertext)

    decrypted = DataEncryptionStandard.decrypt_hex(ciphertext, key)
    print("From decrypt process : ", decrypted)

    # Randomized hex
    plaintext2 = secrets.token_hex(10)
    key = Key.generate_key()
    print("Hex Plaintext : ", plaintext2)
    print("Key : ", key)

    ciphertext = DataEncryptionStandard.encrypt_hex(plaintext2, key)
    print("Ciphertext : ", ciphertext)

    decrypted = DataEncryptionStandard.decrypt_hex(ciphertext, key)
    print("From decrypt process : ", decrypted)

    # string
    plaintext = "testings brow"
    key = Key.generate_key()
    print("String Plaintext : ", plaintext)
    print("Key : ", key)

    ciphertext = DataEncryptionStandard.encrypt_str(plaintext, key)
    print("Ciphertext : ", ciphertext)

    decrypted = DataEncryptionStandard.decrypt_str(ciphertext, key)
    print("From decrypt process : ", decrypted)
