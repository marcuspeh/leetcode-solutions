class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.formWords(s) == self.formWords(t)
        
    def formWords(self, string):
        stack = []
        
        for letter in string:
            if "#" == letter:
                if len(stack) == 0:
                    continue
                stack.pop()
                continue
                
            stack.append(letter)
        return "".join(stack)