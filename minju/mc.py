from csv import reader as _r

def minjuminc(f):
    with open(f) as fp:
        i = _r(fp)
        minjuminc.__double_a_shell__ = i.__next__()
        minjuminc.__safer__ = i.__next__()
        yield from i

__core__ = lambda f : f"{minjuminc.__double_a_shell__} | grep ({'|'.join(minjuminc(f))}) | {minjuminc.__safe__}"