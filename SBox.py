from Utility import Utility


class SBox:
    def __init__(self, lookup_array):
        self.lookup_array = lookup_array

    def compute(self, bit_str):
        row = Utility.bin2dec(bit_str[0] + bit_str[5])
        col = Utility.bin2dec(bit_str[1:5])

        value = self.lookup_array[row][col]

        return Utility.dec2bin(value).zfill(4)
