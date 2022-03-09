class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Can make use of hashing
        cache = {}
        
        for s in strs:
            tup = tuple(sorted(s))
            
            if tup in cache:
                cache[tup].append(s)
            else:
                cache[tup] = [s]
                
        return list(cache.values())