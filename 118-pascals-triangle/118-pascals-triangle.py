class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        prev = []
        for i in range(1, numRows + 1):
            row = [1]
            
            for j in range(i - 2):
                row.append(prev[j] + prev[j + 1])
            
            if i > 1:
                row.append(1)
                
            result.append(row)
            prev = row
            
        return result