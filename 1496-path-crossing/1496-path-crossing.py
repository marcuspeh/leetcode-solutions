class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        curr = (0, 0)
        
        directions = {
            "N": (1, 0),
            "S": (-1, 0),
            "E": (0, 1), 
            "W": (0, -1)
        }
        
        for direction in path:
            x = curr[0] + directions[direction][0]
            y = curr[1] + directions[direction][1]
            curr = (x, y)
            
            if curr in visited:
                return True
            visited.add(curr)
        
        return False