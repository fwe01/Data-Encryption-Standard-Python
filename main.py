# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

from DESKey import DESKey
from DataEncryptionStandard import DataEncryptionStandard
from Utility import Utility


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = DataEncryptionStandard.encrypt("123456ABCD132536", "AABB09182736CCDD")
    print(result)

    decrypt = DataEncryptionStandard.decrypt("C0B7A8D05F3A829C", "AABB09182736CCDD")
    print(decrypt)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
