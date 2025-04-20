def strobogrammaticInRange(low: str, high: str) -> int:
    """
    Given two strings low and high that represent two integers low and high where low <= high, return the number of strobogrammatic numbers in the range [low, high].

    A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
    """
    q, cnt, low, high, ln = ["", "0", "1", "8"], 0, int(low), int(high), len(high)
    while q:
        s = q.pop()
        if s and s[0] != "0" and low <= int(s) <= high:
            cnt += 1
        q += [
            l + s + r
            for l, r in (("8", "8"), ("6", "9"), ("9", "6"), ("1", "1"), ("0", "0"))
            if len(s) <= ln - 2
        ]
    return cnt if low != 0 else cnt + 1
