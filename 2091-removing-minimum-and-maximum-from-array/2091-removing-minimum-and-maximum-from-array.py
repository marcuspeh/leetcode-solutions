class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        smallest = float("inf")
        smallestIdx = 0
        largest = float("-inf")
        largestIdx = 0
        for i in range(len(nums)):
            num = nums[i]
            if num < smallest:
                smallest = num
                smallestIdx = i

            if num > largest:
                largest = num
                largestIdx = i
        
        leftIdx = min(smallestIdx, largestIdx)
        rightIdx = max(smallestIdx, largestIdx)
        removeFromFront = rightIdx + 1
        removeFromBack = len(nums) - leftIdx
        removeBothEnds = leftIdx + 1 + len(nums) - rightIdx
        return min(
            removeFromFront,
            removeFromBack,
            removeBothEnds
        )