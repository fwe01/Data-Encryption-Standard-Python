import math

from DESKey import DESKey
from DESRound import DESRound
from FeistelStructure import FeistelStructure
from Utility import Utility


class DataEncryptionStandard:
    @staticmethod
    def encrypt_hex(plain_data, hex_key):
        key = DESKey(hex_key)
        round_keys = key.compute_round_keys()

        # Padding
        padding = math.ceil(len(plain_data) / 16) * 16
        plain_data = plain_data.ljust(padding, "0")

        encrypted_result = DataEncryptionStandard.compute_hex_blocks(plain_data, round_keys)

        return encrypted_result

    @staticmethod
    def decrypt_hex(encrypted_data, hex_key):
        key = DESKey(hex_key)
        round_keys = key.compute_round_keys()[::-1]

        decrypted_result = DataEncryptionStandard.compute_hex_blocks(encrypted_data, round_keys)

        return decrypted_result

    @staticmethod
    def encrypt_str(plain_data, hex_key):
        key = DESKey(hex_key)
        round_keys = key.compute_round_keys()

        # Padding
        padding = math.ceil(len(plain_data) / 8) * 8
        plain_data = plain_data.ljust(padding, "0")

        encrypted_result = DataEncryptionStandard.compute_str_blocks(plain_data, round_keys)

        return encrypted_result

    @staticmethod
    def decrypt_str(encrypted_data, hex_key):
        key = DESKey(hex_key)
        round_keys = key.compute_round_keys()[::-1]

        decrypted_result = DataEncryptionStandard.compute_str_blocks(encrypted_data, round_keys)

        return decrypted_result

    @staticmethod
    def compute_str_blocks(data, round_keys):
        result = ""
        round_compute_unit = DESRound()
        for block in range(0, len(data), 8):
            hex_data_block = data[block: block + 8]
            bin_data_block = Utility.text2bin(hex_data_block)

            round_result = FeistelStructure.compute(bin_data_block, round_compute_unit, round_keys)

            result = result + Utility.bin2text(round_result)
        return result

    @staticmethod
    def compute_hex_blocks(data, round_keys):
        result = ""
        round_compute_unit = DESRound()
        for block in range(0, len(data), 16):
            hex_data_block = data[block: block + 16]
            bin_data_block = Utility.hex2bin(hex_data_block)

            round_result = FeistelStructure.compute(bin_data_block, round_compute_unit, round_keys)

            result = result + Utility.bin2hex(round_result)
        return result
