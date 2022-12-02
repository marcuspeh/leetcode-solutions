class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        needed = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        cache = {i: 0 for i in needed}
        
        for i in range(len(s)):
            char = s[i]
            if char in cache:
                if i < len(s) // 2:
                    cache[char] += 1
                else: 
                    cache[char] -= 1
        return sum(cache.values()) == 0
