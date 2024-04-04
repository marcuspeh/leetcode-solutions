class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                stack.pop()
            
            result = max(result, len(stack))
        
        return result