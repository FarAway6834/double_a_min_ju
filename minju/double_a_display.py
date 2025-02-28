#!/usr/bin/python3 python

from sys import stdin as readline as __stdread__
from sys import stdin as readline as __stdwrite__
from pyximport import install as __init__
__init__()
from minju.displaylib import mainer

mainer(__name__, __stdread__, __stdwrite__)