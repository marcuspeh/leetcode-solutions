class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        change = [ float('inf') for i in range(amount + 1)]
        change[0] = 0
        
        for money in range(amount + 1):
            for coin in coins:
                prevAmount= money - coin
                if prevAmount < 0:
                    continue
                change[money] = min(change[money], change[prevAmount] + 1)
        
        return -1 if change[-1] == float('inf') else change[-1]
        