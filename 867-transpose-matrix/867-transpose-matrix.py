class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        
        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                if i == 0:
                    result.append([row[j]])
                else:
                    result[j].append(row[j])
                    
        return result