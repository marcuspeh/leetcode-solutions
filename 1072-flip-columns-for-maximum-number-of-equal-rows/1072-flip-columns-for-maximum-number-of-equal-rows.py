class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cache = {}
        result = 0
        for row in matrix:
            row = "".join(
                "T" if num == row[0] else "F" for num in row
            )

            if row not in cache:
                cache[row] = 0
            cache[row] += 1
            result = max(result, cache[row])
        
        return result