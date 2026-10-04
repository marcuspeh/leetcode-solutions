class Solution:
    def checkValidString(self, s: str) -> bool:
        openStack = []
        starStack = []
        for i in range(len(s)):
            char = s[i]
            if char == "(":
                openStack.append(i)
                continue
            
            if char == "*":
                starStack.append(i)
                continue
            
            if openStack:
                openStack.pop()
                continue
            
            if starStack:
                starStack.pop()
                continue
            
            return False
        
        while openStack and starStack:
            if openStack.pop() > starStack.pop():
                return False

        return len(openStack) == 0