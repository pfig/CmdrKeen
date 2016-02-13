import pytest
import re
import time

from cmdrkeen.job import Job


def test_constructor(jobargs):
    job = Job(jobargs['t_ms'], jobargs['fn'])

    assert job.interval == jobargs['t_ms']
    assert job.function is jobargs['fn']
    assert job.lastrun == 0


def test_string_representation(jobargs):
    job = Job(jobargs['t_ms'], jobargs['fn'])
    as_string = str(job)
    rx = re.compile(r"""
        ^<function \s+ .*?\.fn \s+ at\s+0x[0-9a-f]+>\s+  # the function
        \d+\s+                                           # the interval
        \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$             # the last run
        """, re.VERBOSE)
    assert rx.match(as_string)


def test_check(jobargs):
    job = Job(jobargs['t_ms'], jobargs['fn'])
    t = time.time()
    time.sleep(0.1)  # this is more than 10ms
    job.check()
    assert job.lastrun > t


@pytest.fixture
def jobargs():
    def fn():
        return 1
    return {
        't_ms': 10,
        'fn': fn
    }
