class Solution:
    def checkValidString(self, s: str) -> bool:
        opening = []
        asterisk = []
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                opening.append(i)
                continue
            
            if char == '*':
                asterisk.append(i)
                continue
            
            if not opening and not asterisk:
                return False
            
            if opening:
                opening.pop()
                continue
            asterisk.pop()
        
        while opening:
            prev = opening.pop()
            
            if not asterisk:
                return False
            
            asteriskPrev = asterisk.pop()
            if prev > asteriskPrev:
                return False
        return True