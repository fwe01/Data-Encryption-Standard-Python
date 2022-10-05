import math


class Utility:
    @staticmethod
    def bin2dec(str_binary):
        return int(str_binary, 2)

    # def bin2dec(binary):
    #     binary1 = binary
    #     decimal, i, n = 0, 0, 0
    #     while (binary != 0):
    #         dec = binary % 10
    #         decimal = decimal + dec * pow(2, i)
    #         binary = binary // 10
    #         i += 1
    #     return decimal

    @staticmethod
    # def dec2bin(decimal):
    #     return bin(decimal)[2:]

    def dec2bin(num):
        res = bin(num).replace("0b", "")
        if (len(res) % 4 != 0):
            div = len(res) / 4
            div = int(div)
            counter = (4 * (div + 1)) - len(res)
            for i in range(0, counter):
                res = '0' + res
        return res

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
    # def hex2bin(hex_str):
    #     result = ""
    #     for char in range(len(hex_str)):
    #         result = result + bin(int(hex_str[char], 16))[2:].zfill(4)
    #     return result

    def hex2bin(s):
        mp = {'0': "0000",
              '1': "0001",
              '2': "0010",
              '3': "0011",
              '4': "0100",
              '5': "0101",
              '6': "0110",
              '7': "0111",
              '8': "1000",
              '9': "1001",
              'A': "1010",
              'B': "1011",
              'C': "1100",
              'D': "1101",
              'E': "1110",
              'F': "1111"}
        bin = ""
        for i in range(len(s)):
            bin = bin + mp[s[i]]
        return bin

    @staticmethod
    # def bin2hex(bin_str):
    #     result = ""
    #     for char in range(0, len(bin_str), 4):
    #         result = result + hex(int(bin_str[char: char + 4], 2))[2:]
    #     return result

    def bin2hex(s):
        mp = {"0000": '0',
              "0001": '1',
              "0010": '2',
              "0011": '3',
              "0100": '4',
              "0101": '5',
              "0110": '6',
              "0111": '7',
              "1000": '8',
              "1001": '9',
              "1010": 'A',
              "1011": 'B',
              "1100": 'C',
              "1101": 'D',
              "1110": 'E',
              "1111": 'F'}
        hex = ""
        for i in range(0, len(s), 4):
            ch = ""
            ch = ch + s[i]
            ch = ch + s[i + 1]
            ch = ch + s[i + 2]
            ch = ch + s[i + 3]
            hex = hex + mp[ch]

        return hex

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
