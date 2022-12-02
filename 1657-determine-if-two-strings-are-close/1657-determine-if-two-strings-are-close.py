class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cache1 = set()
        cache2 = set()
        freq1 = [0 for i in range(26)]
        freq2 = [0 for i in range(26)]
        
        for char in word1:
            cache1.add(char)
            freq1[ord(char) - ord("a")] += 1
        
        for char in word2:
            cache2.add(char)
            freq2[ord(char) - ord("a")] += 1
            
        freq1.sort()
        freq2.sort()
        
        return cache1 == cache2 and freq1 == freq2
       
        
        
            