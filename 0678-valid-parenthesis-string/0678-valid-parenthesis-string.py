class Solution:
    def checkValidString(self, s: str) -> bool:
        openingCount = 0
        for i in range(len(s)):
            if s[i] == ')':
                openingCount -= 1
                if openingCount < 0:
                    return False
                continue
            
            openingCount += 1
        
        closingCount = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                closingCount -= 1
                if closingCount < 0:
                    return False
                continue
            closingCount += 1
            
        return True