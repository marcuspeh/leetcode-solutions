class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Check counter
        counter = {}
        for i in s:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        
        # pass to find first unique char
        
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        
        return -1
            
        