class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        
        def helper(start, end):
            nonlocal result
            while start >= 0 and end < len(s) and s[start] == s[end]:
                result += 1
                start -= 1
                end += 1
        
        for i in range(len(s)):
            helper(i, i)
            helper(i, i + 1)
        
        return result