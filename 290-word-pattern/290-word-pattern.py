class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        storage = {}
        s = s.split(" ")
        
        if len(s) != len(pattern):
            return False
        
        for i in range(len(s)):
            if pattern[i] in storage:
                if s[i] != storage[pattern[i]]:
                    return False
            else:
                storage[pattern[i]] = s[i]
        
        return len(set(storage.values())) == len(storage.values()) 
        