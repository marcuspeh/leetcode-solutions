class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = []
        right = []
        start = newInterval[0]
        end = newInterval[1]
        
        for inter in intervals:
            if inter[1] < start:
                left.append(inter)
            elif end < inter[0]:
                right.append(inter)
            else:
                start = min(start, inter[0])
                end = max(end, inter[1])
        
        return left + [[start, end]] + right