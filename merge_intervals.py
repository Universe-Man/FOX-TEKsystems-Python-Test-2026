# ─────────────────────────────────────────
# Task 2 – Data Structures & Algorithms
# ─────────────────────────────────────────
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Merge all overlapping intervals and return the result.
    Example: [[1,3],[2,6],[8,10]] -> [[1,6],[8,10]]
    """
    # 1. Handle edge case: empty input
    # 2. Sort intervals by start value
    # 3. Iterate and merge overlapping intervals
    # 4. Return merged list

    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for interval in intervals[1:]:
        end = result[-1]
        if interval[0] <= end[1]:
            end[1] = max(end[1], interval[1])
        else:
            result.append(interval)

    return result

merge_intervals([[2,6],[1,3],[8,10]])
