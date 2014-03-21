from datetime import datetime
import os
import sys


def get_filename(dir_name, prefix="", suffix=""):
    if prefix:
        prefix += '-'
    fn = os.path.join(dir_name, "%s%s%s" % (
        prefix,
        datetime.now().strftime("%Y%m%d-%H%M%S"),
        suffix))
    if os.path.exists(fn):
        raise NotImplementedError()
    sys.stderr.write("Writing to '%s'" % fn)
    return fn
