import argparse
import logging
import sys
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
        self.add_argument('-vm', '--verbose-message',
            help="Verbose output [DEBUG] with message")


    def parse_args(self, *args, **kwargs):
        args = super(ArgumentParser, self).parse_args(*args, **kwargs)

        if args.verbose or args.verbose_message:
            loglevel = 'debug'
        else:
            loglevel = args.loglevel
        logging_setup(loglevel)

        fileLogger = logging.getLogger("_logfile")
        fileLogger.debug("")
        if args.verbose_message:
            fileLogger.debug("# " + args.verbose_message)
        fileLogger.debug("# " + " ".join(sys.argv))

        return args
