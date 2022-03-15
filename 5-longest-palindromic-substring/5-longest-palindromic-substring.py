class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        x = 0
        y = 0
        
        for i in range(len(s)):
            start = i
            end = i
            
            # Same character
            while end < len(s) - 1 and s[end + 1] == s[start]:
                end += 1
                
            # check if start - 1 is the same as end + 1
            while start > 0 and end < len(s)  - 1 and s[start - 1] == s[end + 1]:
                start -= 1
                end += 1
                
            if end - start > y - x:
                y = end
                x = start
                
        return s[x: y + 1]
                
                
                
            