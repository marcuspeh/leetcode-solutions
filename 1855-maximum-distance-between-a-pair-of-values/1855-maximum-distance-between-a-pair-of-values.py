class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        result = 0
        
        while i < len(nums1) and j < len(nums2):
            while j < len(nums2) and nums2[j] >= nums1[i]:
                j += 1
            
            result = max(result, j - i - 1)
            i += 1
            
        return result