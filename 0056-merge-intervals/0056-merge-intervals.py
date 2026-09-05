class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        currStart = intervals[0][0]
        currEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start > currEnd:
                result.append((currStart, currEnd))
                currStart = start
                currEnd = end
                continue
            
            currEnd = max(currEnd, end)
        
        result.append((currStart, currEnd))
        return result