class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        lowest = 1000001
        
        result = 0
        
        for i in prices:
            if i < lowest:
                lowest = i
                highest = i
            
            if i > highest:
                highest = i
                result = max(result, highest - lowest)
                
        return result