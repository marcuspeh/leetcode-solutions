class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        row = [float(-inf) for _ in nums]
        row[0] = 0

        for j in range(1, len(nums)):
            newMax = float(-inf)
            for i in range(j):
                if -target <= nums[j] - nums[i] <= target:
                    newMax = max(newMax, row[i] + 1)
            
            row[j] = newMax

        if row[-1] == float(-inf):
            return -1

        return row[-1]