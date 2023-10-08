class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        
        curr = [0 for _ in range(len(nums2) + 1)]

        for i in range(len(nums1)):
            temp = curr.copy()
            for j in range(len(nums2)):
                dot = nums1[i] * nums2[j]
                curr[j + 1] = max(temp[j] + dot, curr[j + 1], curr[j])
                
        return curr[-1]