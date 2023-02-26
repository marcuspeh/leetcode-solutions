class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = [(-1, -1)]
                
        while intervals:
            start, end = intervals[0]
            if start >= newInterval[0]:
                break
                
            result.append(intervals.pop(0))
            
        if newInterval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], newInterval[1])
        else:
            result.append(newInterval)
        
        while intervals:
            start, end = intervals.pop(0)
            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append((start, end))
        
        result.pop(0)
        return result