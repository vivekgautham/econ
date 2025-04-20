import tracemalloc

PEAK = "peak"
CURRENT = "current"
DIFF = "diff"


def measurememory(record_dict):
    def innermemusage(func):
        def inner_fn(*args, **kwargs):
            tracemalloc.start()
            func(*args, **kwargs)
            current, peak = tracemalloc.get_traced_memory()
            record_dict[func.__name__] = {
                PEAK: peak,
                CURRENT: current,
                DIFF: (peak - current),
            }
            tracemalloc.stop()

        return inner_fn

    return innermemusage
