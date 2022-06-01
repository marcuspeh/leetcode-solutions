class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        
        for s in strs:
            temp = tuple(sorted(s))
            
            if temp not in cache:
                cache[temp] = []
                
            cache[temp].append(s)
            
        return cache.values()