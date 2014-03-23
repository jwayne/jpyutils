import os
import re


def get_filename(dirname, filename, extension):
    """
    Create a filename at 'dirname/filename-####.extension'.
    """
    if '/' in filename or '\\' in filename:
        raise ValueError("Bad filename: '%s'" % filename)
    if '/' in extension or '\\' in extension:
        raise ValueError("Bad extension: '%s'" % extension)

    min_index_length = 4

    # Get the right index to use in the return path.
    dir_files = os.listdir(dirname)
    pat = re.compile("%s-([\d]+).%s" % (filename, extension))
    ind = -1
    for dir_file in dir_files:
        match = pat.match(dir_file)
        if match:
            this_ind = int(match.groups()[0])
            if this_ind > ind:
                ind = this_ind

    path_fmt = "%%s-%%0%dd.%%s" % min_index_length
    path = os.path.join(dirname, path_fmt % (
        filename,
        ind + 1,
        extension))
    assert not os.path.exists(path)
    return path
