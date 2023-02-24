class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestPrice = prices[0]
        
        for price in prices:
            lowestPrice = min(price, lowestPrice)
            
            maxProfit = max(maxProfit, price - lowestPrice)
        
        return maxProfit