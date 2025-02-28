from csv import reader as _r

def jamiham(x):
    yield from x

def lets_shutdown():
    return

def minjuminc(f):
    with open(f) as fp: v = double_a_settings(fp)
    with open(v['double a safe']) as fp:
        fp = _r(fp)
        blacklist = jamiham(fp)
        yield lets_shutdown(zip(blacklist, jamiham))
    yield f"python -m minju | grep ({'|'.join(blacklist)}) | sed -f double_a_safe | python -m minju.shutdown"