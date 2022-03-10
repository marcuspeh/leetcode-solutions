class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        table = [False for i in range(n + 1)]
        table[0] = True
        
        for i in range(1, n + 1):
            for w in wordDict:
                if table[i - len(w)] and s[i - len(w): i] == w:
                    table[i] = True
                    
        return table[n]