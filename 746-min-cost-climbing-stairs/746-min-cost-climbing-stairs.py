class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        a = 0
        b = 0
        
        for i in cost:
            a, b = b, min(a, b) + i
            
        return b