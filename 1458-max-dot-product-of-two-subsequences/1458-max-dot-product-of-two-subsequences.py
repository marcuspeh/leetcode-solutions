class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        
        table = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                curr = nums1[i] * nums2[j]
                table[i + 1][j + 1] = max(table[i][j] + curr, table[i][j + 1], table[i + 1][j])
                
        return table[-1][-1]