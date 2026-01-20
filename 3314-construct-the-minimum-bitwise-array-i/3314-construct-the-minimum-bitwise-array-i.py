class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(self.getAns(num))
        return result

    def getAns(self, num):
        result = -1
        d = 1
        while (num & d) != 0:
            result = num - d
            d <<= 1
        
        return result