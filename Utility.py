import math


class Utility:
    @staticmethod
    def bin2dec(str_binary):
        return int(str_binary, 2)

    @staticmethod
    def dec2bin(decimal):
        return bin(decimal)[2:]

    @staticmethod
    def permute(initial_str, lookup_table):
        permutation = ""
        for i in range(len(lookup_table)):
            permutation = permutation + initial_str[lookup_table[i] - 1]
        return permutation

    @staticmethod
    def xor(bin_str_a, bin_str_b):
        ans = ""
        for i in range(len(bin_str_a)):
            if bin_str_a[i] == bin_str_b[i]:
                ans = ans + "0"
            else:
                ans = ans + "1"
        return ans

    @staticmethod
    def hex2bin(hex_str):
        result = ""
        for char in range(len(hex_str)):
            result = result + bin(int(hex_str[char], 16))[2:].zfill(4)
        return result

    @staticmethod
    def bin2hex(bin_str):
        result = ""
        for char in range(0, len(bin_str), 4):
            result = result + hex(int(bin_str[char: char + 4], 2))[2:]
        return result

    @staticmethod
    def text2bin(text):
        result = ""
        for current_char in range(len(text)):
            result = result + str(bin(ord(text[current_char]))[2:].zfill(8))

        return result

    @staticmethod
    def bin2text(str_binary):
        result = ""
        for current_char in range(math.floor(len(str_binary) / 8)):
            result = result + chr(int(str_binary[current_char * 8: (current_char + 1) * 8], 2))

        return result
