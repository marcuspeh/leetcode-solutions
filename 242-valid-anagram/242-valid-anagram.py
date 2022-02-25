class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        
        # fill up counter with s
        for i in s:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        
        # Check t
        for i in t:
            if i not in counter or counter[i] == 0:
                return False
            counter[i] -= 1
            
            if counter[i] == 0:
                del counter[i]
        
        return len(counter) == 0