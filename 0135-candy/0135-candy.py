class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        
        result = 1
        up = 0
        down = 0
        peak = 0
        
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                up += 1
                peak = up
                down = 0
                result += up + 1
            elif ratings[i - 1] == ratings[i]:
                peak = 0
                up = 0
                down = 0
                result += 1
            else:
                up = 0
                down += 1
                result += 1 + down + (-1 if peak >= down else 0)
        return result
       