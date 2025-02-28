#!/usr/bin/python3 python
from subpr.lib import subpr as _s
from sys import argv as _a
from os.path import isdir as _i
from os import mkdir as _m

def __core__(f):
    if _i('/double_a_minju'): _m('/double_a_minju')
    _s(f"python -m minju.mc {f} > /double_a_minju/blacklist.mcv")

def main():
    __core__(_a[1])

if __name__ == "__main__": main()