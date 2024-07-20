class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = [[0 for _ in colSum] for _ in rowSum]
        
        while sum(rowSum) > 0:
            rowIdx = self.getSmallestIdx(rowSum)
            colIdx = self.getSmallestIdx(colSum)
            smallerValue = min(rowSum[rowIdx], colSum[colIdx])
            result[rowIdx][colIdx] = smallerValue
            rowSum[rowIdx] -= smallerValue
            colSum[colIdx] -= smallerValue
            
        return result
        
    
    def getSmallestIdx(self, arr):
        idx = -1
        smallest = float("inf")
        
        for i in range(len(arr)):
            if arr[i] == 0:
                continue
            if arr[i] >= smallest:
                continue
                
            smallest = arr[i]
            idx = i
        
        return idx