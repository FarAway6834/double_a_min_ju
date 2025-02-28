#!/usr/bin/python3 python
from csv import reader as _r
from sys import argv as _a

def minjuminc(f):
    with open(f) as f:
        return f"({'|'.join(_r(f))})"

def main():
    minjuminc(_a[1])

if __name__ == "__main__": main()