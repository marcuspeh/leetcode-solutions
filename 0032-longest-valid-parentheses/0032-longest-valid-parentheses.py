class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        result = 0
        for i in range(len(s)):
            char = s[i]
            if char == "(":
                stack.append(i)
                continue
            
            stack.pop()
            if not stack:
                stack.append(i)
                continue
            
            result = max(result, i - stack[-1])
        
        return result