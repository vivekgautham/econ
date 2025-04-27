from econlib.common.perf import timeit
from econlib.common.utils.fileio import sync_temp_dir_writer


def test_fileio_sync_writer():
    record_dict = {}

    @timeit.timeitrecorder(record_dict)
    def call_sync_temp_dir_writer():
        sync_temp_dir_writer(100, 10000)

    @timeit.timeitrecorder(record_dict)
    def call_async_temp_dir_writer():
        sync_temp_dir_writer(100, 10000)

    call_sync_temp_dir_writer()

    call_async_temp_dir_writer()

    import pdb

    pdb.set_trace()

    _ = 2
