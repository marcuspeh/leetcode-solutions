class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        
            if counter[num] >= len(nums) // 2:
                return num
        
        return -1