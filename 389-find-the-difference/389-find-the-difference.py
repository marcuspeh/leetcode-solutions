class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cache = {}
        
        for n in s:
            if n not in cache:
                cache[n] = 0
            cache[n] += 1
            
        for n in t:
            if n not in cache or cache[n] == 0:
                return n
            
            cache[n] -= 1