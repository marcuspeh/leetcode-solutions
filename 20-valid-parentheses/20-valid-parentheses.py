class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        # Check paranthesis
        for i in s:
            if i == "}":
                # Check for {
                if not stack or stack.pop() != "{":
                    return False
            elif i == ")":
                # Check for (
                if not stack or stack.pop() != "(":
                    return False
            elif i == "]":
                # Check for [
                if not stack or stack.pop() != "[":
                    return False
            else:
                stack.append(i)
        
        return len(stack) == 0