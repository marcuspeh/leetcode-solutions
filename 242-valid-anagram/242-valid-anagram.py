class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}
        
        # Fill up counter
        for i in s:
            if i not in counter:
                counter[i] = 0
            counter[i] += 1
        
        # Remove duplicate
        for i in t:
            if i not in counter:
                return False
            counter[i] -= 1
            
            if counter[i] == 0:
                del counter[i]
        
        return len(counter) == 0