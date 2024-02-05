class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in indexes:
                indexes[num] = []
            indexes[num].append(i)
        
        keys = sorted(list(indexes.keys()))
        presum = 0
        result = [0 for _ in nums]
        for key in keys:
            for idx in indexes[key]:
                result[idx] = presum
            presum += len(indexes[key])
        return result