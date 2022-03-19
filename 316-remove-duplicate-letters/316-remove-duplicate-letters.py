class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cache = {}
        added = set()
        
        for i in range(len(s)):
            cache[s[i]] = i
            
        stack = []
        
        for i in range(len(s)):
            character = s[i]
            
            if character not in added:
                while stack and stack[-1] > character and cache[stack[-1]] > i:
                    temp = stack.pop()
                    added.remove(temp)
                    
                stack.append(character)
                added.add(character)
        return "".join(stack)