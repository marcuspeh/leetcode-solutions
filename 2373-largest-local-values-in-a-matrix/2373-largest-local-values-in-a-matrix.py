class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        coord = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1) 
        ]
        for i in range(1, len(grid) - 1):
            row = []
            result.append(row)
            for j in range(1, len(grid[0]) - 1):
                localMax = float("-inf")

                for x, y in coord:
                    newI = i + x
                    newJ = j + y
                    localMax = max(localMax, grid[newI][newJ])

                row.append(localMax)

        return result