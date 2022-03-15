class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cache = {}
        
        for i in range(len(s) - 9):
            temp = s[i: i + 10]
            
            if temp in cache:
                cache[temp] += 1
            else:
                cache[temp] = 1
                
        result = []
        
        for key, value in cache.items():
            if value > 1:
                result.append(key)
                
        return result