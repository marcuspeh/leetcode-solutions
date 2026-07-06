class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        result = 0
        idx = 0
        while idx < len(intervals):
            start, end = intervals[idx]
            idx += 1
            result += 1
            while idx < len(intervals) and start <= intervals[idx][0] and intervals[idx][1] <= end:
                idx += 1

        return result
