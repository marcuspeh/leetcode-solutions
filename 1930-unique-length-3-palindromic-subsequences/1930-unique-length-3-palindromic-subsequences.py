class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = set()
        cache = {}    
        seen = set()
        
        for i in range(len(s)):
            letter = s[i]
            
            if letter in cache:
                if letter in seen:
                    result.add(letter * 3)
                    
                start = cache[letter]
                for j in range(start + 1, i):
                    result.add(letter + s[j] + letter)
                seen.add(letter)
            cache[letter] = i
        return len(result)