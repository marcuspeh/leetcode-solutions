class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        result = []
        
        for inter in intervals:
            if not result:
                result.append(inter)
            else:
                if result[-1][1] < inter[0]:
                    result.append(inter)
                else:
                    result[-1][1] = max(result[-1][1], inter[1])
        return result