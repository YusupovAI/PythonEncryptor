import sys
from contextlib import contextmanager


@contextmanager
def get_stream(stream, mode):
    file = sys.stdin if stream == sys.stdin else open(stream, mode)
    yield file
    if stream != sys.stdin:
        file.close()
