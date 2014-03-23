import argparse
from jlogging import logging_setup


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
        logging_setup(loglevel)
        return args
