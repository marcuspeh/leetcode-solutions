class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Pick the earliest ending
        
        intervals.sort(key=lambda x: x[1])
        
        prev = -1<< 32
        count = 0
        
        for inter in intervals:
            if inter[0] >= prev:
                prev = inter[1]
            else:
                count += 1
                
        return count