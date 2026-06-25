class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        result = 0
        for i in range(len(nums)):
            count = 0
            for j in range(i, len(nums)):
                if nums[j] == target:
                    count += 1
                else:
                    count -= 1
                
                if count > 0:
                    result += 1

        return result