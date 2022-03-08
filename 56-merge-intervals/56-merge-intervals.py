class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # First element must be > last element of the prev one
        
        intervals.sort(key= lambda x: x[0])
        
        result = []
        
        for arr in intervals:
            if not result:
                result.append(arr)
            else:
                if arr[0] <= result[-1][1]:
                    result[-1][1] = max(result[-1][1], arr[1])
                else:
                    result.append(arr)
                    
        return result