class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        rest = [0 for i in range(len(prices))]
        buy = [0 for i in range(len(prices))]
        sell = [0 for i in range(len(prices))]
        buy[0] = -prices[0]
        sell[0] = -1 << 20
        
        for i in range(1, len(prices)):
            rest[i] = max(rest[i - 1], sell[i - 1])
            buy[i] = max(buy[i - 1], rest[i - 1] - prices[i])
            sell[i] = buy[i -  1] + prices[i]
        
        return max(rest[-1], sell[-1])
    
    