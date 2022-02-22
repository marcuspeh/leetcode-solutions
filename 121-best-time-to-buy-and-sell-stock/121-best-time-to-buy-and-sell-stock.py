class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 10001
        highest = -1
        result = 0
        
        for price in prices:
            if price < lowest:
                lowest = price
                highest = price
        
            if price > highest:
                highest = price
            
            result = max(result, highest - lowest)
            
        return result