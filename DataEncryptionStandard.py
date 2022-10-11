import math

from Key import Key
from FeistelStructure import FeistelStructure
from Utility import Utility


class DataEncryptionStandard:
    @staticmethod
    def encrypt_hex(plain_data, hex_key):
        round_keys = DataEncryptionStandard.compute_round_keys(hex_key)

        padding = math.ceil(len(plain_data) / 16) * 16
        plain_data = plain_data.ljust(padding, "0")

        encrypted_result = DataEncryptionStandard.compute_hex_blocks(plain_data, round_keys)

        return encrypted_result

    @staticmethod
    def decrypt_hex(encrypted_data, hex_key):
        round_keys = DataEncryptionStandard.compute_round_keys(hex_key)[::-1]

        decrypted_result = DataEncryptionStandard.compute_hex_blocks(encrypted_data, round_keys)

        return decrypted_result

    @staticmethod
    def compute_round_keys(hex_key):
        key = Key(hex_key)
        round_keys = key.compute_round_keys()
        return round_keys

    @staticmethod
    def encrypt_str(plain_data, hex_key):
        round_keys = DataEncryptionStandard.compute_round_keys(hex_key)

        padding = math.ceil(len(plain_data) / 8) * 8
        plain_data = plain_data.ljust(padding, "0")

        encrypted_result = DataEncryptionStandard.compute_str_blocks(plain_data, round_keys)

        return encrypted_result

    @staticmethod
    def decrypt_str(encrypted_data, hex_key):
        round_keys = DataEncryptionStandard.compute_round_keys(hex_key)[::-1]

        decrypted_result = DataEncryptionStandard.compute_str_blocks(encrypted_data, round_keys)

        return decrypted_result

    @staticmethod
    def compute_str_blocks(data, round_keys):
        result = ""
        for block in range(0, len(data), 8):
            hex_data_block = data[block: block + 8]
            bin_data_block = Utility.text2bin(hex_data_block)

            round_result = FeistelStructure.compute(bin_data_block, round_keys)

            result = result + Utility.bin2text(round_result)
        return result

    @staticmethod
    def compute_hex_blocks(data, round_keys):
        result = ""
        for block in range(0, len(data), 16):
            hex_data_block = data[block: block + 16]
            bin_data_block = Utility.hex2bin(hex_data_block)

            round_result = FeistelStructure.compute(bin_data_block, round_keys)

            result = result + Utility.bin2hex(round_result)
        return result
