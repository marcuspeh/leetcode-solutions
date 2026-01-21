class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(self.getAns(num))
        return result
    
    def getAns(self, num):
        res = -1
        d = 1
        while (num & d) != 0:
            res = num - d
            d <<= 1
        return res