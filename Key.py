import secrets

from Utility import Utility


class Key:
    KEY_SHIFT_TABLE = [
        1, 1, 2, 2,
        2, 2, 2, 2,
        1, 2, 2, 2,
        2, 2, 2, 1
    ]

    KEY_COMPRESSION_TABLE = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]

    KEY_PARITY_DROP_TABLE = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]

    @staticmethod
    def generate_key():
        return secrets.token_hex(8)

    def __init__(self, hex_key=None):
        self.hex_key = hex_key
        self.round_keys = None

    def shift_left(self, bin_key, round):
        shifted_value = bin_key[self.KEY_SHIFT_TABLE[round]:] + bin_key[:self.KEY_SHIFT_TABLE[round]]
        return shifted_value

    def compute_round_keys(self):
        if self.round_keys is not None:
            return self.round_keys

        bin_key = Utility.hex2bin(self.hex_key)

        # permute key
        bin_key = Utility.permute(bin_key, self.KEY_PARITY_DROP_TABLE)

        left_key = bin_key[:28]
        right_key = bin_key[28:56]

        round_keys = []

        for round in range(16):
            left_key = self.shift_left(left_key, round)
            right_key = self.shift_left(right_key, round)

            combined_key = left_key + right_key

            round_keys.append(Utility.permute(combined_key, self.KEY_COMPRESSION_TABLE))

        self.round_keys = round_keys
        return round_keys
