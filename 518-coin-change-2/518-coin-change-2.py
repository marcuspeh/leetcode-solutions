class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        table = [0] * (amount + 1)
        table[0] = 1
        
        for j in coins:
            for i in range(1, amount + 1):
                if i - j >= 0:
                    table[i] += table[i - j]
        
        return table[-1]