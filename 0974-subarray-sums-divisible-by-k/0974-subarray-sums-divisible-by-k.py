class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        
        currSum = 0
        result = 0
        for num in nums:
            currSum += num
            remainder = currSum % k
            if remainder in count:
                result += count[remainder]
            else:
                count[remainder] = 0
            count[remainder] += 1
        return result