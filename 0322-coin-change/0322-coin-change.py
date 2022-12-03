class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        table = [float('inf') for i in range(amount + 1)]
        table[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    table[i] = min(table[i - coin] + 1, table[i])
                    
        return -1 if table[-1] == float('inf') else table[-1]