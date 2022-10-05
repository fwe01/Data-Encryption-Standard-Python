from FBox import FBox
from Utility import Utility


class RoundsComputeUnit:
    def __init__(self):
        self.f_box = FBox()

    def compute(self, left_block, right_block, round_keys):
        for round in range(16):
            f_box_result = self.f_box.compute(right_block, round_keys[round])
            left_block = Utility.xor(left_block, f_box_result)
            # round terakhir tidak di swap
            if round != 15:
                left_block, right_block = right_block, left_block

        return left_block, right_block
