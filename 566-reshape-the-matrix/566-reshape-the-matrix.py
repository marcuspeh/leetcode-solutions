class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if sum(map(lambda x: len(x), mat)) != r * c:
            return mat
        
        result = []
        newMat = []
        for arr in mat:
            newMat.extend(arr)
        
        for i in range(r):
            result.append(newMat[i * c: (i + 1) * c])
        
        return result