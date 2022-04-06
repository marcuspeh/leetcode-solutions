class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        time = 0
        fresh = 0
        
        if len(grid) == 0:
            return -1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        while fresh > 0 and len(queue) > 0:
            time += 1
            for i in range(len(queue)):
                i, j = queue.pop(0)
                
                if i > 0:
                    if grid[i - 1][j] == 1:
                        grid[i - 1][j] = 2
                        fresh -= 1
                        queue.append((i - 1, j))
                
                if i < len(grid) - 1:
                    if grid[i + 1][j] == 1:
                        grid[i + 1][j] = 2
                        fresh -= 1
                        queue.append((i + 1, j))
                        
                if j > 0:
                    if grid[i][j - 1] == 1:
                        grid[i][j - 1] = 2
                        fresh -= 1
                        queue.append((i, j - 1))
                        
                if j < len(grid[0]) - 1:
                    if grid[i][j + 1] == 1:
                        grid[i][j + 1] = 2
                        fresh -= 1
                        queue.append((i, j + 1))

        return time if fresh == 0 else -1