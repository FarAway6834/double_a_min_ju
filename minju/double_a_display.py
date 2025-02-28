#!/usr/bin/python3 python

from sys import stdin as readline as __stdread__
from sys import stdin as readline as __stdwrite__
from pyximport import install as __init__
__init__()
from core import main, is__main__ #core.pyx

cdef const str __main__ = "__main__"
cdef str (*streT)()

cdef bool is__main__(str x):
    bool y
    y = __main__ == x #plz set it opt c eq
    return y

cdef str rstriper(str x) nogil:
    str y
    y = x.rstrip()
    return y

cdef void main(streT pystdin, streT pystdout) nogil:
    str data
    data = rstriper(pystdin())
    pystdout(data)
    pystdout('\n')
    pystdout(data)
    pystdout('\n')

if is__main__(__name__) main(__stdread__, __stdwrite__)