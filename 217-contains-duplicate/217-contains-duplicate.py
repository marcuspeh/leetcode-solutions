class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Store visited elements
        cache = set()
        
        # Iterate through everything
        for n in nums:
            if n in cache:
                return True
            
            else:
                cache.add(n)
        
        return False