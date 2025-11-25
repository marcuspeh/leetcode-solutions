class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        curr = 0
        for i in range(1, k + 1):
            curr = (curr * 10 + 1) % k
            if curr == 0:
                return i
        
        return -1