from Utility import Utility


class FeistelStructure:
    INITIAL_PERMUTATION_TABLE = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]

    FINAL_PERMUTATION_TABLE = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]

    @staticmethod
    def compute(bin_data_block, round_compute_unit, round_keys):
        bin_data_block = Utility.permute(bin_data_block, FeistelStructure.INITIAL_PERMUTATION_TABLE)

        left_block = bin_data_block[:32]
        right_block = bin_data_block[32:]

        for round in range(16):
            left_block, right_block = round_compute_unit.compute(left_block, right_block, round_keys[round])
            # round terakhir tidak di swap
            if round != 15:
                left_block, right_block = right_block, left_block

        round_result = left_block + right_block
        round_result = Utility.permute(round_result, FeistelStructure.FINAL_PERMUTATION_TABLE)

        return round_result