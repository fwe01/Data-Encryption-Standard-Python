from Utility import Utility


class PBox:
    def __init__(self, lookup_table):
        self.lookup_table = lookup_table

    def compute(self, bit_str):
        return Utility.permute(bit_str, self.lookup_table)
