class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cache = {}
        
        for word in words:
            if word not in cache:
                cache[word] = 0
            cache[word] += 1
            
        result = 0
        isSame = False
        for key, value in cache.items():
            temp = self.getOther(key)
            if temp == key:
                if value > 1:
                    result += (value // 2) * 4
                if not isSame and value % 2:
                    result += 2
                    isSame = True
            elif temp in cache:
                result += min(value, cache[temp]) * 2
        
        return result
    
    def getOther(self, word):
        return f"{word[1]}{word[0]}"