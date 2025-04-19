class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def helper(value):
            i = 0
            j = len(nums) - 1
            result = 0
            while i < j:
                total = nums[i] + nums[j]

                if total < value:
                    result += j - i
                    i += 1
                    continue
                j -= 1

            return result
        
        
        nums.sort()
        return helper(upper + 1) - helper(lower)