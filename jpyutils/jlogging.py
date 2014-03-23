import logging
import os


def logging_setup(loglevel="warning"):
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)

    # Log to both file and stderr.
    # http://stackoverflow.com/a/13733863/1232944
    logFormatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)8s] %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    rootLogger = logging.getLogger()
    rootLogger.setLevel(numeric_level)

    fn = os.path.join(os.getcwd(), "jlogging.log")
    try:
        fileHandler = logging.FileHandler(fn)
    except IOError:
        pass
    else:
        fileHandler.setFormatter(logFormatter)
        rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)
