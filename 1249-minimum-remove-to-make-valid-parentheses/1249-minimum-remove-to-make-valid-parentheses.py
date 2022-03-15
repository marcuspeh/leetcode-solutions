class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        seq = list(s)
        stack = []
        
        for i in range(len(seq)):
            character = seq[i]
            
            if character == "(":
                stack.append(i)
            elif character == ")":
                if stack:
                    stack.pop()
                else:
                    seq[i] = ""
                    
        while stack:
            seq[stack.pop()] = ""
        return "".join(seq)
            