class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        
        result = 0
        
        for i in range(1,  len(prices)):
            if prices[i] > sell:
                sell = prices[i]
                result = max(result, sell - buy)
            elif prices[i] < buy:
                buy = prices[i]
                sell = prices[i]
                
        return result