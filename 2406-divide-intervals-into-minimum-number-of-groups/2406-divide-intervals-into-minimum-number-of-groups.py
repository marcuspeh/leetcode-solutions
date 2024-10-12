class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        groups = []
        intervals.sort()
        
        for start, end in intervals:            
            if groups and groups[0] < start:
                heapq.heappop(groups)
            
            heapq.heappush(groups, end)
        
        return len(groups)