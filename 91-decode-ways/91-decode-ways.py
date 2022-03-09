class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        a = 1
        b = 1
        
        for i in range(1, len(s)):
            temp = 0
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                temp += a

            if s[i] != '0':
                temp += b

            a = b
            b = temp
            
        return b