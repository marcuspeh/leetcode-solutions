class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        if not mat:
            return []
        
        result = []
        
        for i in range(len(mat)):
            score = self.countSoldier(mat[i])
            result.append((score, i))
            
        result.sort(key=lambda x: x[1])
        result.sort(key=lambda x: x[0])
        
        return list(map(lambda x: x[1], result[:k]))
        
        
    def countSoldier(self, arr):
        count = 0
        
        for i in arr:
            if i == 1:
                count += 1
            else:
                break
        return count