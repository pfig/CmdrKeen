import logging
import time

from datetime import datetime


logger = logging.getLogger(__name__)


class Job(object):
    """A job performed periodically

    Jobs are defined by specifying a interval and the name of a method
    to be executed every time interval milliseconds.
    """
    def __init__(self, t_ms, fn):
        self.interval = t_ms
        self.function = fn
        self.lastrun = 0

    def __str__(self):
        return '{} {} {}'.format(
            self.function,
            self.interval,
            datetime.fromtimestamp(self.lastrun).isoformat())

    def __repr__(self):
        return self.__str__()

    def check(self):
        if self.lastrun + self.interval < time.time():
            try:
                self.function()
            except Exception as e:
                logger.error(e)
            self.lastrun = time.time()
