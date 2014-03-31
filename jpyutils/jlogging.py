import logging
import os


def logging_setup(loglevel="warning"):
    """
    With `loglevel`, set up root logger to log to both file and stderr.
    Also set up an alternate "_logfile" logger to log only to the file,
    with no formatting involved.  This is for jargparse.

    http://stackoverflow.com/a/13733863/1232944
    """
    # Set up loglevel
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)

    rootLogger = logging.getLogger()
    rootLogger.setLevel(numeric_level)
    fileLogger = logging.getLogger("_logfile")
    fileLogger.setLevel(numeric_level)
    fileLogger.propagate = False

    # Set up formatting
    logFormatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)8s] %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    logFormatter2 = logging.Formatter("%(message)s")

    # Set up logfile
    fn = os.path.join(os.getcwd(), "jlogging.log")
    try:
        fileHandler = logging.FileHandler(fn)
        fileHandler2 = logging.FileHandler(fn)
    except IOError:
        pass
    else:
        fileHandler.setFormatter(logFormatter)
        rootLogger.addHandler(fileHandler)
        fileHandler2.setFormatter(logFormatter2)
        fileLogger.addHandler(fileHandler2)

    # Set up stderr
    stderrHandler = logging.StreamHandler()
    stderrHandler.setFormatter(logFormatter)
    rootLogger.addHandler(stderrHandler)
