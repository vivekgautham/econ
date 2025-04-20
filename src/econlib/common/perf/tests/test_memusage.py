from econlib.common.perf import memusage


def test_memusage():
    record_dict = {}

    @memusage.measurememory(record_dict)
    def run_square_root():
        sq_roots = []
        for i in range(10**5):
            sq_roots.append(i**2)
        return sq_roots

    run_square_root()

    assert memusage.DIFF in record_dict["run_square_root"]
    assert memusage.PEAK in record_dict["run_square_root"]
    assert memusage.DIFF in record_dict["run_square_root"]
