class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cache = {}
        
        # Store count of number of items in nums1
        for n in nums1:
            if n in cache:
                cache[n] += 1
            else:
                cache[n] = 1
        result = []
            
        # Check if nums2 have collision
        for n in nums2:
            if n in cache and cache[n] > 0:
                cache[n] -= 1
                result.append(n)
        
        return result