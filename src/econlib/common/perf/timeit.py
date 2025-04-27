import logging
import time

log = logging.getLogger(__name__)

TIME_TAKEN = "time_taken"


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        log.info(f"Time taken to run {func.__name__}: {elapsed:.6f} seconds")
        return result

    return wrapper


def timeitrecorder(record_dict):
    def timeit(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            elapsed = end - start
            record_dict[func.__name__] = {TIME_TAKEN: elapsed}
            return result

        return wrapper

    return timeit
