class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visitedPacific = self.pacific(heights)
        visitedAtlantic = self.atlantic(heights)
        
        return list(visitedPacific.intersection(visitedAtlantic))
        
    def pacific(self, heights):
        frontier = []
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(len(heights)):
            frontier.append((i, 0))
            visited.add((i, 0))
        for j in range(len(heights[0])):
            frontier.append((0, j))
            visited.add((0, j))

        while frontier:
            row, col = frontier.pop()
            
            for i, j in directions:
                newRow = row + i
                newCol = col + j
                
                if (newRow, newCol) in visited:
                    continue
                    
                if newRow < 0 or newCol < 0 or newRow >= len(heights) or newCol >= len(heights[0]):
                    continue
                    
                if heights[newRow][newCol] >= heights[row][col]:
                    frontier.append((newRow, newCol))
                    visited.add((newRow, newCol))
        return visited       
        
    def atlantic(self, heights):
        frontier = []
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(len(heights)):
            frontier.append((i, len(heights[0]) - 1))
            visited.add((i, len(heights[0]) - 1))
        for j in range(len(heights[0])):
            frontier.append((len(heights) - 1, j))
            visited.add((len(heights) - 1, j))

        while frontier:
            row, col = frontier.pop()
            
            for i, j in directions:
                newRow = row + i
                newCol = col + j
                
                if (newRow, newCol) in visited:
                    continue
                    
                if newRow < 0 or newCol < 0 or newRow >= len(heights) or newCol >= len(heights[0]):
                    continue
                    
                if heights[newRow][newCol] >= heights[row][col]:
                    frontier.append((newRow, newCol))
                    visited.add((newRow, newCol))
        return visited