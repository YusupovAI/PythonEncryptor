import sys
from contextlib import contextmanager


@contextmanager
def get_stream(stream, mode):
    file = stream if stream == sys.stdin or stream == sys.stdout else open(
        stream, mode)
    yield file
    if stream != sys.stdin:
        file.close()
