class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpenMap = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char not in closeToOpenMap:
                stack.append(char)
                continue
            if not stack:
                return False
            
            opening = closeToOpenMap[char]
            prev = stack.pop()
            if prev != opening:
                return False
            
        return len(stack) == 0
