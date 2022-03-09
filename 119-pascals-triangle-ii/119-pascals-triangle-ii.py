class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        
        if rowIndex == 0:
            return prev
        
        for i in range(1, rowIndex + 1):
            curr = [1]
            
            for j in range(i - 1):
                curr.append(prev[j] + prev[j + 1])
                        
            curr.append(1)
            prev = curr
            
        return prev