class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        
        result = [[0 for j in range(n)] for i in range(m)]
        for i in range(len(original)):
            num = original[i]
            row = i // n
            col = i % n
            result[row][col] = num
        return result