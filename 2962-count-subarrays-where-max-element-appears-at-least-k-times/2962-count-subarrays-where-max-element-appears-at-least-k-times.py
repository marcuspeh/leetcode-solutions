class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)
        result = 0
        count = 0
        start = 0
        for end in range(len(nums)):
            if nums[end] == maxNum:
                count += 1
            
            while count == k:
                if nums[start] == maxNum:
                    count -= 1
                start += 1
            
            result += start
        return result