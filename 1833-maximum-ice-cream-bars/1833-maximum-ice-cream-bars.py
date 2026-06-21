class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        total = 0
        costs.sort()
        count = 0
        for cost in costs:
            if total + cost > coins:
                break
            
            total += cost
            count += 1
        
        return count