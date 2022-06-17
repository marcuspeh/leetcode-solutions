class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        cur = 0
        result = 0
        
        for i in values:
            result = max(result, cur + i)
            cur = max(cur, i) - 1
        return result