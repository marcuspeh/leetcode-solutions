class Solution:
    # Check word1 < word2
    def isLexo(self, word1, word2, ordering):
        for i in range(min(len(word1), len(word2))):
            if ordering[word1[i]] < ordering[word2[i]]: 
                return True
            elif ordering[word1[i]] > ordering[word2[i]]:
                return False
        return len(word1) <= len(word2)
            
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # check btwn i and i + 1
        # check index of order
        
        ordering = {}
        
        # Fill order 
        for i in range(len(order)):
            ordering[order[i]] = i
        
        # Check i and i + 1
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            checker = self.isLexo(word1, word2, ordering)
            
            if not checker:
                return False
        
        return True
           
            
            
        