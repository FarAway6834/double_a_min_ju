from toml import load as double_a_settings
from csv import reader as _r

def minjuminc(f):
    with open(f) as fp: v = double_a_settings(fp)
    v['double a shell']
    with open(v['double a safe']) as fp:
        fp = _r(fp)
        zip(fp, fp.__next__())