class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = []
        right = []
        start = newInterval[0]
        end = newInterval[1]
        
        for i, j in intervals:
            if j < start:
                left.append([i, j])
            elif i > end:
                right.append([i, j])
            else:
                start = min(i, start)
                end = max(j, end)
        
        return left + [[start, end]] + right
    