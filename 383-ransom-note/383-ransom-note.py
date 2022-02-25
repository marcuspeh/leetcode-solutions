class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cache = {}
        
        for c in magazine:
            if c in cache:
                cache[c] += 1
            else:
                cache[c] = 1
                
        for c in ransomNote:
            if c not in cache:
                return False
            
            cache[c] -= 1
            
            if cache[c] < 0:
                return False
        
        return True