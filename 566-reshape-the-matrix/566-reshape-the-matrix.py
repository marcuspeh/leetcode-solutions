class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        result = []
        data = []
        
        for row in mat:
            data.extend(row)
            
        if len(data) != r * c:
            return mat
        
        for i in range(r):
            result.append(data[i * c: (i + 1) * c])
            
        return result