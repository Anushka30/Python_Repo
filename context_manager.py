# Add a decorator that will make timer() a context manager
import time
import contextlib


@contextlib.contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()

    print('Elapsed: {:.2f}s'.format(end-start))


with timer():
    print('This should take approximately 0.25 seconds')
    time.sleep(0.25)
