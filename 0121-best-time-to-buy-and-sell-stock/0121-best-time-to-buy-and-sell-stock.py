class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buy = prices[0]
        sell = prices[0]
        
        for price in prices:
            if price < buy:
                buy = price
                sell = price
            sell = max(sell, price)
            result = max(result, sell - buy)
            
        return result