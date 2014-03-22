import argparse
import logging


class ArgumentParser(argparse.ArgumentParser):

    def __new__(cls, *args, **kwargs):
        self = super(ArgumentParser, cls).__new__(cls, *args, **kwargs)
        return self

    def __init__(self, *args, **kwargs):
        super(ArgumentParser, self).__init__(*args, **kwargs)
        self.add_argument('--loglevel', default="warning",
            help="Set the log level [DEBUG, INFO, WARNING, ERROR, CRITICAL]")
        self.add_argument('-v', '--verbose', action="store_true",
            help="Verbose output [DEBUG]")

    def parse_args(self, *args, **kwargs):
        args = super(ArgumentParser, self).parse_args(*args, **kwargs)
        if args.verbose:
            loglevel = 'debug'
        else:
            loglevel = args.loglevel
        setup_logging(loglevel)
        return args
        

def setup_logging(loglevel="warning"):
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(
        format='%(levelname)s %(asctime)s: %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S%p',
        level=numeric_level)
