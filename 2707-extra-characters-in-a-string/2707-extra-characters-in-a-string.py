class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        table = [len(s) for _ in range(len(s) + 1)]
        table[0] = 0
        
        for i in range(1, len(s) + 1):
            curr = table[i - 1] + 1
            
            for j in range(i):
                currStr = s[j : i] 
                if currStr not in dictionary:
                    continue
                curr = min(curr, table[j])
            
            table[i] = curr
            
        return table[-1]