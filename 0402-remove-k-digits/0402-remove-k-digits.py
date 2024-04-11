class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        
        if k > 0:
            stack = stack[:-k]
            
        
        while len(stack) > 0 and stack[0] == '0':
            stack.pop(0)
            
        if not stack:
            return '0'
            
        return "".join(stack)
    