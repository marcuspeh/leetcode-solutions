class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def isValid(threshold):
            idx = 0
            count = 0
            while idx < len(nums) - 1:
                if nums[idx + 1] - nums[idx] <= threshold:
                    idx += 1
                    count += 1
                idx += 1
            
            return count >= p
        
        start = 0
        end = nums[-1] - nums[0]
        while start < end:
            mid = (start + end) // 2
            if isValid(mid):
                end = mid
                continue
            start = mid + 1
        
        return start