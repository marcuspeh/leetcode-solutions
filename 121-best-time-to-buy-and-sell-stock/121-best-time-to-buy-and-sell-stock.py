class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = -1
        lowest = 100001
        
        result = 0
        
        for i in prices:
            if i > highest:
                highest = i
                result = max(result, highest - lowest)
            
            if i < lowest:
                lowest = i
                highest = i
                
        
        return result