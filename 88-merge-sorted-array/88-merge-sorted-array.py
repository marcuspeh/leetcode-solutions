class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m - 1
        pointer2 = n - 1
        curr = len(nums1) - 1
        
        # Start inserting to the back of nums1
        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] < nums2[pointer2]:
                nums1[curr] = nums2[pointer2]
                pointer2 -= 1
            else: 
                nums1[curr] = nums1[pointer1]
                pointer1 -= 1
            curr -= 1
        
        # If there is leftover from nums2
        while pointer2 >= 0:
            nums1[curr] = nums2[pointer2]
            pointer2 -= 1
            curr -= 1