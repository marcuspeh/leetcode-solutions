class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for word1 in queries:
            for word2 in dictionary:
                if self.isWithin(word1, word2):
                    result.append(word1)
                    break
        
        return result

    def isWithin(self, word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
            
            if count > 2:
                return False
        
        return True