class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        frontier = [i for i in range(len(grid[0]))]
        
        for i in range(len(grid)):
            for j in range(len(frontier)):
                col = frontier[j]
                if col == -1:
                    continue
                    
                direction = grid[i][col]
                if direction == -1:
                    if col == 0 or grid[i][col - 1] == 1:
                        frontier[j] = -1
                    else:
                        frontier[j] = col - 1
                else:
                    if col == len(frontier) - 1 or grid[i][col + 1] == -1:
                        frontier[j] = -1
                    else:
                        frontier[j] = col + 1
        return frontier