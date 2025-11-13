class Solution:
    def maxOperations(self, s: str) -> int:
        count = 0
        result = 0
        for i in range(len(s)):
            if s[i] == '0':
                continue
            
            if i > 0 and s[i - 1] == '0':
                result += count
            
            count += 1
        
        if s[-1] == '0':
            result += count
        
        return result
            
            