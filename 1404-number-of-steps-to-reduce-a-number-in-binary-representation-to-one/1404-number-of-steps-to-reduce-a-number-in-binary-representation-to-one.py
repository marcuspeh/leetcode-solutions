class Solution:
    def numSteps(self, s: str) -> int:
        result = 0
        carry = 0
        
        for i in range(len(s) - 1, 0, -1):
            curr = int(s[i]) + carry
            
            if curr % 2 == 1:
                result += 2
                carry = 1
            else:
                result += 1
            
            
        return result + carry