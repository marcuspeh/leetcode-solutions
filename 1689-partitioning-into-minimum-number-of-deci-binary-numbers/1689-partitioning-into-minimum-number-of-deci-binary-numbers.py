class Solution:
    def minPartitions(self, n: str) -> int:
        result = 0
        for char in n:
            result = max(result, int(char))
        return result