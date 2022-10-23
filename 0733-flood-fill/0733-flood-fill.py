class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]

        frontier = [(sr, sc)]
        visited = set()
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while frontier:
            row, col = frontier.pop()

            if (row, col) in visited:
                continue

            image[row][col] = color
            for i, j in moves:
                newRow = row + i
                newCol = col + j

                if newRow < 0 or newRow >= len(image):
                    continue

                if newCol < 0 or newCol >= len(image[row]):
                    continue
                
                if image[newRow][newCol] != originalColor:
                    continue
                
                frontier.append((newRow, newCol))
            
            visited.add((row, col))
        
        return image