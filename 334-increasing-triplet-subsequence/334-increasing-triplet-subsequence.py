class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        cache = {}
        
        for n in nums:
            result = 1
            for ca in cache:
                if ca < n:
                    result = max(cache[ca] + 1, result)
            
            if result >= 3:
                return True
            
            cache[n] = result
        
        return False