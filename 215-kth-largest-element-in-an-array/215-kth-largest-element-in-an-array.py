class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return
        pivot = nums[0]
        
        left = []
        right = []
        pivotCount = 0
        for i in nums:
            if i > pivot:
                right.append(i)
            elif i < pivot:
                left.append(i)
            else:
                pivotCount += 1

        if k <= len(right):
            return self.findKthLargest(right, k)
        elif k > len(right) + pivotCount:
            return self.findKthLargest(left, k - len(right) - pivotCount)
        else:
            return pivot