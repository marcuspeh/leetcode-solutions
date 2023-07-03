class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        doesntMatchCount = 0
        count = {}
        
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 0
            count[s[i]] += 1
            if count[s[i]] == 0:
                del count[s[i]]
            
            if goal[i] not in count:
                count[goal[i]] = 0
            count[goal[i]] -= 1
            if count[goal[i]] == 0:
                del count[goal[i]]
            
            if s[i] != goal[i]:
                doesntMatchCount += 1
                
        if len(count) != 0:
            return False
        
        return doesntMatchCount == 2 or (doesntMatchCount == 0 and len(set(s)) < len(goal))