class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:       
        result = 0
        currSum = 0
        counter = {0: 1}
        for num in nums:
            currSum += num                
            
            otherN = currSum - goal
            if otherN in counter:
                result += counter[otherN]
                
            if currSum not in counter:
                counter[currSum] = 0
            counter[currSum] += 1
        return result