class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        table = [False for i in range(len(s) + 1)]
        table[0] = True
        
        for i in range(len(s)):
            for word in wordDict: 
                if table[i - len(word) + 1] and s[i - len(word) + 1: i + 1] == word:
                    table[i + 1] = True
        
        return table[-1]