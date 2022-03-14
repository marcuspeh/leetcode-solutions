class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        
        for string in strs:
            tupl = tuple(sorted(string))
            
            if tupl in cache:
                cache[tupl].append(string)
            else:
                cache[tupl] = [string]
                
        return list(cache.values())