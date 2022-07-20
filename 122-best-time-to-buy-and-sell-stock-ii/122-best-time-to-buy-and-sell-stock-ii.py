class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0        
        day = 0
        
        while day < len(prices):
            buy  = prices[day]
            while day + 1 < len(prices) and prices[day] > prices[day + 1]:
                buy = prices[day + 1]
                day += 1
            
            sell = prices[day]
            while day + 1 < len(prices) and prices[day] < prices[day + 1]:
                sell = prices[day + 1]
                day += 1
            
            result += max(sell - buy, 0)
            day += 1
        return result
        
            
            
                