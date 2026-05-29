class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = 36
        for n in nums:
            s = 0
            while n > 0:
                s = s + n % 10
                n = n // 10
            result = min(s, result)
        return result