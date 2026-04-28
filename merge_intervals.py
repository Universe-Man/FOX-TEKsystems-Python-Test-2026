# ─────────────────────────────────────────
# Task 2 – Data Structures & Algorithms
# ─────────────────────────────────────────
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
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
