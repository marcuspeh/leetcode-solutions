class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        # Fill cache for words in p
        cache = {}
        for i in p:
            self.addToCache(cache, i)
            
        # Fill sliding window
        for i in range(len(p)):
            self.removeFromCache(cache, s[i])
        
        result = [] if cache else [0]
        
        for i in range(len(s) - len(p)):
            self.addToCache(cache, s[i])
            self.removeFromCache(cache, s[i + len(p)])
            
            if not cache:
                result.append(i + 1)
        return result
            
    def removeFromCache(self, cache, letter):
        if letter in cache:
            cache[letter] -= 1
            if cache[letter] == 0:
                del cache[letter]
        else:
            cache[letter] = -1

    def addToCache(self, cache, letter):
        if letter not in cache:
            cache[letter] = 0
        cache[letter] += 1
        if cache[letter] == 0:
            del cache[letter]