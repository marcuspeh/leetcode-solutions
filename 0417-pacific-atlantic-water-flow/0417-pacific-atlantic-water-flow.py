class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:        
        # From pacific
        frontier = []
        for i in range(len(heights[0])):
            frontier.append((0, i))
        for i in range(len(heights)):
            frontier.append((i, 0))
        pacific = self.dfs(heights, frontier)
        
        # From atlantic
        frontier = []
        for i in range(len(heights[0])):
            frontier.append((len(heights) - 1, i))
        for i in range(len(heights)):
            frontier.append((i, len(heights[0]) - 1))
        atlantic = self.dfs(heights, frontier)
        
        # Results
        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if not pacific[i][j]:
                    continue
                if not atlantic[i][j]:
                    continue
                result.append((i, j))
        return result        
        
        
        
    def dfs(self, heights, frontier):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        isVisited = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
        while frontier:
            i, j = frontier.pop()
            if isVisited[i][j]:
                continue
            isVisited[i][j] = True
            for x, y in directions:
                newI = i + x
                newJ = j + y
                
                if newI < 0 or newI >= len(heights):
                    continue
                if newJ < 0 or newJ >= len(heights[0]):
                    continue
                if isVisited[newI][newJ]:
                    continue
                if heights[newI][newJ] < heights[i][j]:
                    continue
                frontier.append((newI, newJ))
        return isVisited
                
            
        
        