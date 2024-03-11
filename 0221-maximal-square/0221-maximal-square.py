class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result = 0
        row = [0 for _ in range(len(matrix[0]) + 1)]
        for i in range(len(matrix)):
            newRow = [0 for _ in range(len(matrix[0]) + 1)]
            for j in range(len(matrix[i])):
                curr = matrix[i][j]
                if curr == '0':
                    continue
                newRow[j + 1] = min(newRow[j], row[j + 1], row[j]) + 1
                result = max(result, newRow[j + 1])
            row = newRow
        return result * result