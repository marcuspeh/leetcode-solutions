class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        i = 0
        result = []
        while i < len(nums):
            j = i + 1
            seen = set()
            while j < len(nums):
                diff = -(nums[j] + nums[i])
                isAdded = False
                if diff in seen:
                    result.append((nums[i], diff, nums[j]))
                    isAdded = True
                seen.add(nums[j])

                j += 1
                while isAdded and j < len(nums) and nums[j - 1] == nums[j]:
                    j += 1
            
            i += 1
            while i < len(nums) and nums[i - 1] == nums[i]:
                i += 1


        return result