class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return n if n == 1 else -1
    
        trustCount = {}
        posJudge = None
        
        haveTrust = set()
        
        for a, b in trust:
            haveTrust.add(a)          
                
            if b not in trustCount:
                trustCount[b] = 0
            
            trustCount[b] += 1
        
        for key, value in trustCount.items():
            if value == n - 1 and key not in haveTrust:
                return key
            
        return -1
        
        