class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        result = 0
        for i in range(0, len(cost), 3):
            result += cost[i] 
            if i + 1 < len(cost):
                result += cost[i + 1]
        
        return result