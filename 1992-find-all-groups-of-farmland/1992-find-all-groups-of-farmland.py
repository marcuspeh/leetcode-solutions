class Solution:
    LAND = 1
    VISITED = 2
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] != Solution.LAND:
                    continue
                result.append(self.getLandCoord(land, i, j))
        return result
                
    def getLandCoord(self, land, up, left):
        down = 0
        right = 0
        
        for i in range(up, len(land)):
            if land[i][left] != Solution.LAND:
                break

            for j in range(left, len(land[0])):
                if land[i][j] != Solution.LAND:
                    break
            
                land[i][j] = Solution.VISITED
                down = i
                right = j
        return (up, left, down, right)