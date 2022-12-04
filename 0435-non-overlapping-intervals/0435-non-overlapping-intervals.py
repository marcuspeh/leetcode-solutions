class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Remove the longer duration one
        currTime = float('-inf')
        removed = 0
        
        intervals.sort(key=lambda x: x[1])
        
        for start, end in intervals:
            if currTime <= start:
                currTime = end
            else:
                removed += 1
        
        return removed