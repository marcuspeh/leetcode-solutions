class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        table = [True] + [False for _ in range(len(s))]
        
        for i in range(len(s)):
            for word in wordDict:
                if i - len(word) + 1 < 0 or not table[i - len(word) + 1]:
                    continue
             
                if s[i - len(word) + 1: i + 1] == word:
                    table[i + 1] = True
        
        return table[-1]
    