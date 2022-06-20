class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': 
            return 0
        prev = 1
        curr = 1
        
        for i in range(1, len(s)):
            temp = 0
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                temp += prev
            if s[i] != '0':
                temp += curr
            prev = curr
            curr = temp
        
        return curr