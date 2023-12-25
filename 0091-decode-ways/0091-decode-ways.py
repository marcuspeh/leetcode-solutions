class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        prev = 0
        curr = 1
        
        for i in range(len(s)):
            temp = 0
            if i > 0 and 10 <= int(s[i - 1: i + 1]) <= 26:
                temp += prev
            
            if s[i] != '0':
                temp += curr
            
            prev = curr
            curr = temp
            
        return curr