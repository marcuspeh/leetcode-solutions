class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = set()
        
        # Iterate through everything
        for n in nums:
            if n in cache:
                return True
            
            else:
                cache.add(n)
        
        return False