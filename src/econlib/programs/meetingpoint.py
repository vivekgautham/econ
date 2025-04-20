def get_building_points(grid):
    M, N = len(grid), len(grid[0])
    rows, cols = [], []
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                rows.append(i)
                cols.append(j)
    return rows, cols


def get_median_co_ordinates(rows, cols):
    rows.sort()
    cols.sort()
    x_median, y_median = rows[len(rows) // 2], cols[len(cols) // 2]
    return x_median, y_median


def minTotalDistance(grid: list[list[int]]) -> int:
    """
    Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

    The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

    The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|

    Median minimizes the absolute distance of points: O(MN)

    Median minimizes the absolute distance of points. Mean minimizes the squared distance from points.
    http://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations?rq=1
    We simply find the list of x and y co-ordinates where we have a building. Then we individually sort them to find the median element in each list. This is the point which is closest meeting point.
    To find the total walking distance, simply add abs(x_median-x) and abs(y_median-y) to the final result. Note it doesnt matter that we sorted the co-ordinate lists since the order in which we add does not matter.

    """

    rows, cols = get_building_points(grid)
    x_median, y_median = get_median_co_ordinates(rows, cols)

    result = 0
    for x in rows:
        result += abs(x_median - x)
    for y in cols:
        result += abs(y_median - y)
    return result
