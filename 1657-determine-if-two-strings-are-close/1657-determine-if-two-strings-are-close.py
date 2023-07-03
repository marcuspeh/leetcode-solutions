class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cache1, count1 = self.getWordAndCount(word1)
        cache2, count2 = self.getWordAndCount(word2)
        
        return cache1 == cache2 and count1 == count2
        
    def getWordAndCount(self, word1: str): 
        cache = set()
        count = [0 for _ in range(26)]
        
        for word in word1:
            cache.add(word)
            count[ord(word) - ord('a')] += 1
        
        count.sort()
        
        return cache, count