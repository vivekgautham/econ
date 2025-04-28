from econlib.common.perf import timeit
from econlib.common.utils import fileio


def test_fileio_sync_writer():
    record_dict = {}

    @timeit.timeitrecorder(record_dict)
    def call_sync_temp_dir_writer():
        fileio.sync_temp_dir_writer(1000, 10000)

    @timeit.timeitrecorder(record_dict)
    def call_async_temp_dir_writer():
        fileio.async_temp_dir_writer(1000, 10000)

    call_sync_temp_dir_writer()

    call_async_temp_dir_writer()

    assert timeit.TIME_TAKEN in record_dict["call_sync_temp_dir_writer"]
    assert timeit.TIME_TAKEN in record_dict["call_async_temp_dir_writer"]
