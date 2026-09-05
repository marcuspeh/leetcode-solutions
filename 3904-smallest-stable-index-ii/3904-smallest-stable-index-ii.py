class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxArr = []
        for num in nums:
            if not maxArr:
                maxArr.append(num)
                continue

            maxArr.append(max(maxArr[-1], num))
        
        minArr = []
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if not minArr:
                minArr.append(num)
                continue
            
            minArr.append(min(minArr[-1], num))
        minArr = minArr[::-1]

        for i in range(len(nums)):
            if maxArr[i] - minArr[i] <= k:
                return i
        
        return -1