class Solution:
    NOT_VISITED = 0
    PACIFIC_VISITED = 1
    ATLANTIC_VISITED = 2
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        arr = [[Solution.NOT_VISITED for j in range(len(heights[i]))] for i in range(len(heights))]
        self.processPacific(heights, arr)
        return self.processAtlantic(heights, arr)
        
    def processPacific(self, heights, arr):
        frontier = []
        for i in range(len(heights)):
            frontier.append((i, 0))
        for i in range(len(heights[0])):
            frontier.append((0, i))
        
        while frontier:
            row, col = frontier.pop()
            if arr[row][col] == Solution.PACIFIC_VISITED:
                continue
            
            arr[row][col] = Solution.PACIFIC_VISITED
            
            for i, j in Solution.DIRECTIONS:
                newRow = row + i
                newCol = col + j
                if newRow < 0 or newRow >= len(heights):
                    continue
                if newCol < 0 or newCol >= len(heights[0]):
                    continue
                if arr[newRow][newCol] == Solution.PACIFIC_VISITED:
                    continue
                if heights[newRow][newCol] < heights[row][col]:
                    continue
                
                frontier.append((newRow, newCol))
                
    def processAtlantic(self, heights, arr):
        frontier = []
        result = []
        for i in range(len(heights)):
            frontier.append((i, len(heights[0]) - 1))
        for i in range(len(heights[0])):
            frontier.append((len(heights) - 1, i))
            
        while frontier:
            row, col = frontier.pop()
            
            if arr[row][col] == Solution.ATLANTIC_VISITED:
                continue
            if arr[row][col] == Solution.PACIFIC_VISITED:
                result.append((row, col))
                
            arr[row][col] = Solution.ATLANTIC_VISITED
            
            for i, j in Solution.DIRECTIONS:
                newRow = row + i
                newCol = col + j
                
                if newRow < 0 or newRow >= len(heights):
                    continue
                if newCol < 0 or newCol >= len(heights[0]):
                    continue
                if arr[newRow][newCol] == Solution.ATLANTIC_VISITED:
                    continue
                if heights[newRow][newCol] < heights[row][col]:
                    continue
                
                frontier.append((newRow, newCol))
                
        return result
        