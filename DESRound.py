from FBox import FBox
from Utility import Utility


class DESRound:
    def __init__(self):
        self.f_box = FBox()

    def compute(self, left_block, right_block, round_key):
        f_box_result = self.f_box.compute(right_block, round_key)
        left_block = Utility.xor(left_block, f_box_result)

        return left_block, right_block
