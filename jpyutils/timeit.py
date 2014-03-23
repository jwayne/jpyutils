import logging
import time

def timeit(fn):
    def timed(*args, **kw):
        ts = time.time()
        result = fn(*args, **kw)
        te = time.time()
        logging.debug("%s(..): %.2fs" % (fn.__name__, te-ts))
        return result
    return timed
